````markdown
# Assignment 8: CLI Interface and Production Deployment

## Learning Objectives
- Build professional command-line interfaces with advanced features
- Implement deployment strategies for production applications
- Use containerization with Docker for consistent environments
- Set up monitoring, logging, and health checks
- Apply security hardening and performance optimization
- Deploy applications to cloud platforms

## Background

The final step in professional Python development is creating production-ready applications that can be deployed, monitored, and maintained in real-world environments. This assignment transforms your calculator into a robust, deployable application with enterprise-grade features.

### Production-Ready Software

Production deployment requires consideration of:
- **Reliability**: Error handling, graceful degradation, health checks
- **Scalability**: Performance optimization, resource management
- **Security**: Input validation, secrets management, audit logging
- **Observability**: Monitoring, metrics, structured logging
- **Maintainability**: Clean architecture, documentation, automated deployment

This assignment teaches you to build software that operates reliably in production environments.

## Prerequisites
- Completed Assignments 1-7
- Calculator package with packaging and distribution
- Understanding of containerization concepts
- Basic knowledge of cloud deployment platforms

## Time to Complete
Expect to spend approximately 4-5 hours on this assignment.

## Part 1: Advanced CLI Interface

### Task 1.1: Enhanced CLI with Click Framework

1. Install Click and additional dependencies:
   ```bash
   pip install click rich tabulate
   ```

2. Update `src/calculator/cli_advanced.py`:
   ```python
   """Advanced CLI interface using Click framework."""
   import sys
   import json
   import csv
   from pathlib import Path
   from typing import Optional, List, Dict, Any
   
   import click
   from rich.console import Console
   from rich.table import Table
   from rich.progress import Progress, SpinnerColumn, TextColumn
   from rich.panel import Panel
   from rich.prompt import Prompt, Confirm
   from tabulate import tabulate
   
   from .calculator import Calculator
   from .config import config
   from .logging_config import setup_logging, get_logger
   from .version import __version__
   
   
   console = Console()
   logger = get_logger('cli')
   
   
   # Click context settings
   CONTEXT_SETTINGS = {
       'help_option_names': ['-h', '--help'],
       'max_content_width': 120,
   }
   
   
   @click.group(context_settings=CONTEXT_SETTINGS)
   @click.version_option(version=__version__)
   @click.option('--config-file', type=click.Path(exists=True), 
                 help='Path to configuration file')
   @click.option('--log-level', 
                 type=click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']),
                 default='INFO', help='Set logging level')
   @click.option('--precision', type=click.IntRange(2, 15), 
                 help='Number of decimal places for results')
   @click.option('--quiet', '-q', is_flag=True, help='Suppress output')
   @click.option('--verbose', '-v', is_flag=True, help='Verbose output')
   @click.pass_context
   def cli(ctx, config_file, log_level, precision, quiet, verbose):
       """
       Calculator Pro - Professional calculator with advanced features.
       
       A comprehensive calculator supporting basic arithmetic, scientific operations,
       memory management, and batch processing with enterprise-grade features.
       """
       # Initialize context
       ctx.ensure_object(dict)
       
       # Setup logging
       if verbose:
           log_level = 'DEBUG'
       elif quiet:
           log_level = 'ERROR'
       
       setup_logging(level=log_level)
       
       # Configure precision
       if precision:
           config.calculator.precision = precision
       
       # Initialize calculator
       ctx.obj['calculator'] = Calculator()
       ctx.obj['quiet'] = quiet
       ctx.obj['verbose'] = verbose
       
       logger.info(f"Calculator CLI v{__version__} initialized")
   
   
   @cli.group()
   @click.pass_context
   def calc(ctx):
       """Basic calculator operations."""
       pass
   
   
   @calc.command()
   @click.argument('a', type=float)
   @click.argument('b', type=float)
   @click.option('--format', 'output_format', 
                 type=click.Choice(['number', 'json', 'table']),
                 default='number', help='Output format')
   @click.pass_context
   def add(ctx, a, b, output_format):
       """Add two numbers."""
       calc_instance = ctx.obj['calculator']
       result = calc_instance.add(a, b)
       _output_result('addition', a, b, result, output_format, ctx.obj['quiet'])
   
   
   @calc.command()
   @click.argument('a', type=float)
   @click.argument('b', type=float)
   @click.option('--format', 'output_format', 
                 type=click.Choice(['number', 'json', 'table']),
                 default='number', help='Output format')
   @click.pass_context
   def subtract(ctx, a, b, output_format):
       """Subtract b from a."""
       calc_instance = ctx.obj['calculator']
       result = calc_instance.subtract(a, b)
       _output_result('subtraction', a, b, result, output_format, ctx.obj['quiet'])
   
   
   @calc.command()
   @click.argument('a', type=float)
   @click.argument('b', type=float)
   @click.option('--format', 'output_format', 
                 type=click.Choice(['number', 'json', 'table']),
                 default='number', help='Output format')
   @click.pass_context
   def multiply(ctx, a, b, output_format):
       """Multiply two numbers."""
       calc_instance = ctx.obj['calculator']
       result = calc_instance.multiply(a, b)
       _output_result('multiplication', a, b, result, output_format, ctx.obj['quiet'])
   
   
   @calc.command()
   @click.argument('a', type=float)
   @click.argument('b', type=float)
   @click.option('--format', 'output_format', 
                 type=click.Choice(['number', 'json', 'table']),
                 default='number', help='Output format')
   @click.pass_context
   def divide(ctx, a, b, output_format):
       """Divide a by b."""
       calc_instance = ctx.obj['calculator']
       result = calc_instance.divide(a, b)
       _output_result('division', a, b, result, output_format, ctx.obj['quiet'])
   
   
   @cli.group()
   @click.pass_context
   def scientific(ctx):
       """Scientific calculator operations."""
       pass
   
   
   @scientific.command()
   @click.argument('x', type=float)
   @click.option('--format', 'output_format', 
                 type=click.Choice(['number', 'json', 'table']),
                 default='number', help='Output format')
   @click.pass_context
   def sqrt(ctx, x, output_format):
       """Calculate square root."""
       calc_instance = ctx.obj['calculator']
       result = calc_instance.square_root(x)
       _output_result('square_root', x, None, result, output_format, ctx.obj['quiet'])
   
   
   @scientific.command()
   @click.argument('base', type=float)
   @click.argument('exponent', type=float)
   @click.option('--format', 'output_format', 
                 type=click.Choice(['number', 'json', 'table']),
                 default='number', help='Output format')
   @click.pass_context
   def power(ctx, base, exponent, output_format):
       """Raise base to the power of exponent."""
       calc_instance = ctx.obj['calculator']
       result = calc_instance.power(base, exponent)
       _output_result('power', base, exponent, result, output_format, ctx.obj['quiet'])
   
   
   @cli.group()
   @click.pass_context
   def memory(ctx):
       """Memory operations."""
       pass
   
   
   @memory.command()
   @click.argument('value', type=float)
   @click.pass_context
   def store(ctx, value):
       """Store value in memory."""
       calc_instance = ctx.obj['calculator']
       calc_instance.memory_store(value)
       if not ctx.obj['quiet']:
           console.print(f"[green]Stored {value} in memory[/green]")
   
   
   @memory.command()
   @click.pass_context
   def recall(ctx):
       """Recall value from memory."""
       calc_instance = ctx.obj['calculator']
       value = calc_instance.memory_recall()
       if not ctx.obj['quiet']:
           console.print(f"Memory: {value}")
       else:
           click.echo(value)
   
   
   @memory.command()
   @click.pass_context
   def clear(ctx):
       """Clear memory."""
       calc_instance = ctx.obj['calculator']
       calc_instance.memory_clear()
       if not ctx.obj['quiet']:
           console.print("[yellow]Memory cleared[/yellow]")
   
   
   @cli.command()
   @click.option('--format', 'output_format', 
                 type=click.Choice(['table', 'json', 'csv']),
                 default='table', help='Output format')
   @click.option('--limit', type=int, help='Limit number of entries')
   @click.pass_context
   def history(ctx, output_format, limit):
       """Show calculation history."""
       calc_instance = ctx.obj['calculator']
       history_data = calc_instance.get_history()
       
       if limit:
           history_data = history_data[-limit:]
       
       if not history_data:
           if not ctx.obj['quiet']:
               console.print("[yellow]No history available[/yellow]")
           return
       
       _output_history(history_data, output_format, ctx.obj['quiet'])
   
   
   @cli.command()
   @click.option('--format', 'output_format', 
                 type=click.Choice(['table', 'json']),
                 default='table', help='Output format')
   @click.pass_context
   def stats(ctx, output_format):
       """Show calculator statistics."""
       calc_instance = ctx.obj['calculator']
       stats_data = calc_instance.get_stats()
       _output_stats(stats_data, output_format, ctx.obj['quiet'])
   
   
   @cli.command()
   @click.argument('input_file', type=click.File('r'))
   @click.option('--output', '-o', type=click.File('w'), default='-',
                 help='Output file (default: stdout)')
   @click.option('--format', 'output_format', 
                 type=click.Choice(['json', 'csv', 'table']),
                 default='json', help='Output format')
   @click.pass_context
   def batch(ctx, input_file, output, output_format):
       """Process batch calculations from file.
       
       Input file should contain one calculation per line in format:
       operation arg1 [arg2]
       
       Example:
       add 5 3
       multiply 2 4
       sqrt 16
       """
       calc_instance = ctx.obj['calculator']
       results = []
       
       with Progress(
           SpinnerColumn(),
           TextColumn("[progress.description]{task.description}"),
           console=console,
           disable=ctx.obj['quiet']
       ) as progress:
           task = progress.add_task("Processing calculations...", total=None)
           
           for line_no, line in enumerate(input_file, 1):
               line = line.strip()
               if not line or line.startswith('#'):
                   continue
               
               try:
                   result = _process_batch_line(calc_instance, line)
                   results.append({
                       'line': line_no,
                       'operation': line,
                       'result': result,
                       'status': 'success'
                   })
               except Exception as e:
                   results.append({
                       'line': line_no,
                       'operation': line,
                       'error': str(e),
                       'status': 'error'
                   })
               
               progress.update(task, advance=1)
       
       _output_batch_results(results, output_format, output, ctx.obj['quiet'])
   
   
   @cli.command()
   @click.option('--port', default=8000, help='Port to run on')
   @click.option('--host', default='127.0.0.1', help='Host to bind to')
   @click.pass_context
   def serve(ctx, port, host):
       """Start calculator as a web service."""
       try:
           from .web_server import run_server
           if not ctx.obj['quiet']:
               console.print(f"[green]Starting calculator server on {host}:{port}[/green]")
           run_server(host, port)
       except ImportError:
           console.print("[red]Web server dependencies not installed. Install with: pip install 'calculator-pro[web]'[/red]")
           sys.exit(1)
   
   
   @cli.command()
   @click.pass_context
   def interactive(ctx):
       """Start interactive calculator mode."""
       calc_instance = ctx.obj['calculator']
       
       console.print(Panel(
           f"[bold blue]Calculator Pro v{__version__}[/bold blue]\n"
           "Interactive Mode\n\n"
           "Commands: add, subtract, multiply, divide, sqrt, power, sin, cos, tan\n"
           "Memory: store <value>, recall, clear_memory\n"
           "Utility: history, stats, help, quit",
           title="Welcome"
       ))
       
       while True:
           try:
               command = Prompt.ask("[bold cyan]calc>[/bold cyan]")
               
               if command.lower() in ['quit', 'exit', 'q']:
                   console.print("[green]Goodbye![/green]")
                   break
               
               if command.lower() == 'help':
                   _show_interactive_help()
                   continue
               
               result = _process_interactive_command(calc_instance, command)
               if result is not None:
                   console.print(f"[bold green]Result:[/bold green] {result}")
           
           except KeyboardInterrupt:
               console.print("\n[green]Goodbye![/green]")
               break
           except Exception as e:
               console.print(f"[red]Error:[/red] {e}")
   
   
   def _output_result(operation: str, a: float, b: Optional[float], result: float, 
                     format_type: str, quiet: bool):
       """Output calculation result in specified format."""
       if format_type == 'json':
           data = {
               'operation': operation,
               'operands': [a] if b is None else [a, b],
               'result': result
           }
           click.echo(json.dumps(data, indent=2))
       elif format_type == 'table':
           if b is None:
               table_data = [['Operation', 'Input', 'Result'],
                            [operation, str(a), str(result)]]
           else:
               table_data = [['Operation', 'A', 'B', 'Result'],
                            [operation, str(a), str(b), str(result)]]
           
           if quiet:
               click.echo(tabulate(table_data, headers='firstrow', tablefmt='simple'))
           else:
               table = Table()
               for header in table_data[0]:
                   table.add_column(header, style="cyan")
               table.add_row(*[str(x) for x in table_data[1]])
               console.print(table)
       else:  # number format
           click.echo(result)
   
   
   def _output_history(history_data: List[str], format_type: str, quiet: bool):
       """Output history in specified format."""
       if format_type == 'json':
           data = {'history': history_data}
           click.echo(json.dumps(data, indent=2))
       elif format_type == 'csv':
           writer = csv.writer(sys.stdout)
           writer.writerow(['Entry', 'Calculation'])
           for i, entry in enumerate(history_data, 1):
               writer.writerow([i, entry])
       else:  # table format
           if quiet:
               table_data = [['#', 'Calculation']]
               for i, entry in enumerate(history_data, 1):
                   table_data.append([str(i), entry])
               click.echo(tabulate(table_data, headers='firstrow', tablefmt='simple'))
           else:
               table = Table(title="Calculation History")
               table.add_column("#", style="cyan", width=4)
               table.add_column("Calculation", style="white")
               
               for i, entry in enumerate(history_data, 1):
                   table.add_row(str(i), entry)
               
               console.print(table)
   
   
   def _output_stats(stats_data: Dict[str, Any], format_type: str, quiet: bool):
       """Output statistics in specified format."""
       if format_type == 'json':
           click.echo(json.dumps(stats_data, indent=2))
       else:  # table format
           if quiet:
               table_data = [['Statistic', 'Value']]
               for key, value in stats_data.items():
                   table_data.append([key.replace('_', ' ').title(), str(value)])
               click.echo(tabulate(table_data, headers='firstrow', tablefmt='simple'))
           else:
               table = Table(title="Calculator Statistics")
               table.add_column("Statistic", style="cyan")
               table.add_column("Value", style="white")
               
               for key, value in stats_data.items():
                   table.add_row(key.replace('_', ' ').title(), str(value))
               
               console.print(table)
   
   
   def _process_batch_line(calc_instance: Calculator, line: str) -> float:
       """Process a single line from batch input."""
       parts = line.split()
       if not parts:
           raise ValueError("Empty line")
       
       operation = parts[0].lower()
       
       if operation == 'add' and len(parts) == 3:
           return calc_instance.add(float(parts[1]), float(parts[2]))
       elif operation == 'subtract' and len(parts) == 3:
           return calc_instance.subtract(float(parts[1]), float(parts[2]))
       elif operation == 'multiply' and len(parts) == 3:
           return calc_instance.multiply(float(parts[1]), float(parts[2]))
       elif operation == 'divide' and len(parts) == 3:
           return calc_instance.divide(float(parts[1]), float(parts[2]))
       elif operation == 'sqrt' and len(parts) == 2:
           return calc_instance.square_root(float(parts[1]))
       elif operation == 'power' and len(parts) == 3:
           return calc_instance.power(float(parts[1]), float(parts[2]))
       else:
           raise ValueError(f"Unknown operation or wrong number of arguments: {line}")
   
   
   def _output_batch_results(results: List[Dict], format_type: str, output_file, quiet: bool):
       """Output batch processing results."""
       if format_type == 'json':
           json.dump(results, output_file, indent=2)
       elif format_type == 'csv':
           writer = csv.DictWriter(output_file, fieldnames=['line', 'operation', 'result', 'status', 'error'])
           writer.writeheader()
           writer.writerows(results)
       else:  # table format
           table_data = [['Line', 'Operation', 'Result', 'Status']]
           for result in results:
               if result['status'] == 'success':
                   table_data.append([
                       str(result['line']),
                       result['operation'],
                       str(result['result']),
                       'OK'
                   ])
               else:
                   table_data.append([
                       str(result['line']),
                       result['operation'],
                       result.get('error', 'Unknown error'),
                       'ERROR'
                   ])
           
           output_file.write(tabulate(table_data, headers='firstrow', tablefmt='grid'))
   
   
   def _process_interactive_command(calc_instance: Calculator, command: str) -> Optional[float]:
       """Process an interactive command."""
       parts = command.split()
       if not parts:
           return None
       
       cmd = parts[0].lower()
       
       try:
           if cmd == 'add' and len(parts) == 3:
               return calc_instance.add(float(parts[1]), float(parts[2]))
           elif cmd == 'subtract' and len(parts) == 3:
               return calc_instance.subtract(float(parts[1]), float(parts[2]))
           elif cmd == 'multiply' and len(parts) == 3:
               return calc_instance.multiply(float(parts[1]), float(parts[2]))
           elif cmd == 'divide' and len(parts) == 3:
               return calc_instance.divide(float(parts[1]), float(parts[2]))
           elif cmd == 'sqrt' and len(parts) == 2:
               return calc_instance.square_root(float(parts[1]))
           elif cmd == 'power' and len(parts) == 3:
               return calc_instance.power(float(parts[1]), float(parts[2]))
           elif cmd == 'store' and len(parts) == 2:
               calc_instance.memory_store(float(parts[1]))
               console.print(f"[green]Stored {parts[1]} in memory[/green]")
               return None
           elif cmd == 'recall' and len(parts) == 1:
               return calc_instance.memory_recall()
           elif cmd == 'clear_memory' and len(parts) == 1:
               calc_instance.memory_clear()
               console.print("[yellow]Memory cleared[/yellow]")
               return None
           elif cmd == 'history':
               history_data = calc_instance.get_history()
               _output_history(history_data, 'table', False)
               return None
           elif cmd == 'stats':
               stats_data = calc_instance.get_stats()
               _output_stats(stats_data, 'table', False)
               return None
           else:
               console.print(f"[red]Unknown command:[/red] {command}")
               console.print("Type 'help' for available commands")
               return None
       except ValueError as e:
           console.print(f"[red]Invalid number format:[/red] {e}")
           return None
   
   
   def _show_interactive_help():
       """Show interactive mode help."""
       help_table = Table(title="Available Commands")
       help_table.add_column("Command", style="cyan")
       help_table.add_column("Arguments", style="yellow")
       help_table.add_column("Description", style="white")
       
       commands = [
           ("add", "<a> <b>", "Add two numbers"),
           ("subtract", "<a> <b>", "Subtract b from a"),
           ("multiply", "<a> <b>", "Multiply two numbers"),
           ("divide", "<a> <b>", "Divide a by b"),
           ("sqrt", "<x>", "Square root of x"),
           ("power", "<base> <exp>", "Raise base to power"),
           ("store", "<value>", "Store value in memory"),
           ("recall", "", "Recall value from memory"),
           ("clear_memory", "", "Clear memory"),
           ("history", "", "Show calculation history"),
           ("stats", "", "Show calculator statistics"),
           ("help", "", "Show this help"),
           ("quit", "", "Exit calculator"),
       ]
       
       for cmd, args, desc in commands:
           help_table.add_row(cmd, args, desc)
       
       console.print(help_table)
   
   
   if __name__ == '__main__':
       cli()
   ```

### Task 1.2: Web Server Component

1. Create `src/calculator/web_server.py`:
   ```python
   """Web server for calculator API."""
   import json
   from typing import Dict, Any
   from http.server import HTTPServer, BaseHTTPRequestHandler
   import urllib.parse
   
   from .calculator import Calculator
   from .logging_config import get_logger
   
   
   logger = get_logger('web_server')
   
   
   class CalculatorHandler(BaseHTTPRequestHandler):
       """HTTP request handler for calculator API."""
       
       def __init__(self, *args, **kwargs):
           self.calculator = Calculator()
           super().__init__(*args, **kwargs)
       
       def do_GET(self):
           """Handle GET requests."""
           if self.path == '/health':
               self._handle_health()
           elif self.path == '/stats':
               self._handle_stats()
           elif self.path == '/history':
               self._handle_history()
           elif self.path.startswith('/memory'):
               self._handle_memory_recall()
           else:
               self._send_error(404, "Not Found")
       
       def do_POST(self):
           """Handle POST requests."""
           if self.path == '/calculate':
               self._handle_calculate()
           elif self.path == '/memory/store':
               self._handle_memory_store()
           elif self.path == '/memory/clear':
               self._handle_memory_clear()
           else:
               self._send_error(404, "Not Found")
       
       def _handle_health(self):
           """Health check endpoint."""
           response = {"status": "healthy", "service": "calculator"}
           self._send_json_response(response)
       
       def _handle_stats(self):
           """Statistics endpoint."""
           stats = self.calculator.get_stats()
           self._send_json_response(stats)
       
       def _handle_history(self):
           """History endpoint."""
           history = self.calculator.get_history()
           response = {"history": history}
           self._send_json_response(response)
       
       def _handle_memory_recall(self):
           """Memory recall endpoint."""
           memory_value = self.calculator.memory_recall()
           response = {"memory": memory_value}
           self._send_json_response(response)
       
       def _handle_calculate(self):
           """Calculation endpoint."""
           try:
               content_length = int(self.headers.get('Content-Length', 0))
               post_data = self.rfile.read(content_length)
               data = json.loads(post_data.decode('utf-8'))
               
               operation = data.get('operation')
               operands = data.get('operands', [])
               
               if operation == 'add' and len(operands) == 2:
                   result = self.calculator.add(operands[0], operands[1])
               elif operation == 'subtract' and len(operands) == 2:
                   result = self.calculator.subtract(operands[0], operands[1])
               elif operation == 'multiply' and len(operands) == 2:
                   result = self.calculator.multiply(operands[0], operands[1])
               elif operation == 'divide' and len(operands) == 2:
                   result = self.calculator.divide(operands[0], operands[1])
               elif operation == 'sqrt' and len(operands) == 1:
                   result = self.calculator.square_root(operands[0])
               elif operation == 'power' and len(operands) == 2:
                   result = self.calculator.power(operands[0], operands[1])
               else:
                   self._send_error(400, "Invalid operation or operands")
                   return
               
               response = {
                   "operation": operation,
                   "operands": operands,
                   "result": result
               }
               self._send_json_response(response)
               
           except Exception as e:
               self._send_error(400, str(e))
       
       def _handle_memory_store(self):
           """Memory store endpoint."""
           try:
               content_length = int(self.headers.get('Content-Length', 0))
               post_data = self.rfile.read(content_length)
               data = json.loads(post_data.decode('utf-8'))
               
               value = data.get('value')
               if value is None:
                   self._send_error(400, "Missing value")
                   return
               
               self.calculator.memory_store(value)
               response = {"message": f"Stored {value} in memory"}
               self._send_json_response(response)
               
           except Exception as e:
               self._send_error(400, str(e))
       
       def _handle_memory_clear(self):
           """Memory clear endpoint."""
           self.calculator.memory_clear()
           response = {"message": "Memory cleared"}
           self._send_json_response(response)
       
       def _send_json_response(self, data: Dict[str, Any], status_code: int = 200):
           """Send JSON response."""
           self.send_response(status_code)
           self.send_header('Content-Type', 'application/json')
           self.send_header('Access-Control-Allow-Origin', '*')
           self.end_headers()
           
           response_data = json.dumps(data, indent=2)
           self.wfile.write(response_data.encode('utf-8'))
       
       def _send_error(self, code: int, message: str):
           """Send error response."""
           self.send_response(code)
           self.send_header('Content-Type', 'application/json')
           self.end_headers()
           
           error_data = {"error": message, "code": code}
           response_data = json.dumps(error_data)
           self.wfile.write(response_data.encode('utf-8'))
       
       def log_message(self, format, *args):
           """Override to use our logger."""
           logger.info(f"{self.address_string()} - {format % args}")
   
   
   def run_server(host: str = '127.0.0.1', port: int = 8000):
       """Run the calculator web server."""
       server = HTTPServer((host, port), CalculatorHandler)
       logger.info(f"Calculator server starting on {host}:{port}")
       
       try:
           server.serve_forever()
       except KeyboardInterrupt:
           logger.info("Server stopped by user")
       finally:
           server.server_close()
   ```

## Part 2: Containerization with Docker

### Task 2.1: Create Docker Configuration

1. Create `Dockerfile`:
   ```dockerfile
   # Multi-stage build for optimized production image
   FROM python:3.11-slim as builder
   
   # Set environment variables
   ENV PYTHONDONTWRITEBYTECODE=1 \
       PYTHONUNBUFFERED=1 \
       PIP_NO_CACHE_DIR=1 \
       PIP_DISABLE_PIP_VERSION_CHECK=1
   
   # Install system dependencies
   RUN apt-get update && apt-get install -y \
       build-essential \
       && rm -rf /var/lib/apt/lists/*
   
   # Create wheel
   WORKDIR /build
   COPY pyproject.toml README.md LICENSE CHANGELOG.md ./
   COPY src/ src/
   
   RUN pip install build && python -m build
   
   # Production image
   FROM python:3.11-slim as production
   
   # Set environment variables
   ENV PYTHONDONTWRITEBYTECODE=1 \
       PYTHONUNBUFFERED=1 \
       ENVIRONMENT=production \
       DEBUG=false
   
   # Create non-root user
   RUN groupadd -r calculator && useradd -r -g calculator calculator
   
   # Create directories
   RUN mkdir -p /app/logs /app/data && \
       chown -R calculator:calculator /app
   
   # Install runtime dependencies
   RUN apt-get update && apt-get install -y \
       curl \
       && rm -rf /var/lib/apt/lists/*
   
   # Copy and install wheel
   COPY --from=builder /build/dist/*.whl /tmp/
   RUN pip install /tmp/*.whl && rm /tmp/*.whl
   
   # Copy configuration
   COPY config/ /app/config/
   RUN chown -R calculator:calculator /app/config
   
   # Switch to non-root user
   USER calculator
   WORKDIR /app
   
   # Health check
   HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
       CMD curl -f http://localhost:8000/health || exit 1
   
   # Expose port
   EXPOSE 8000
   
   # Default command
   CMD ["calculator", "serve", "--host", "0.0.0.0", "--port", "8000"]
   ```

2. Create `.dockerignore`:
   ```
   # Git
   .git
   .gitignore
   
   # Python
   __pycache__
   *.pyc
   *.pyo
   *.pyd
   .Python
   env
   pip-log.txt
   pip-delete-this-directory.txt
   .tox
   .coverage
   .coverage.*
   .pytest_cache
   nosetests.xml
   coverage.xml
   *.cover
   *.log
   .cache
   
   # Virtual environments
   .env
   .venv
   venv/
   ENV/
   
   # IDE
   .vscode/
   .idea/
   *.swp
   *.swo
   *~
   
   # OS
   .DS_Store
   Thumbs.db
   
   # Build artifacts
   build/
   dist/
   *.egg-info/
   
   # Documentation
   docs/_build/
   
   # Testing
   .pytest_cache/
   htmlcov/
   
   # Local data
   logs/
   data/
   *.db
   
   # Docker
   Dockerfile*
   docker-compose*
   ```

3. Create `docker-compose.yml`:
   ```yaml
   version: '3.8'
   
   services:
     calculator:
       build: .
       ports:
         - "8000:8000"
       environment:
         - ENVIRONMENT=production
         - LOG_LEVEL=INFO
         - CALC_PRECISION=10
         - LOG_FILE_PATH=/app/logs/calculator.log
       volumes:
         - calculator_logs:/app/logs
         - calculator_data:/app/data
       healthcheck:
         test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
         interval: 30s
         timeout: 3s
         retries: 3
         start_period: 40s
       restart: unless-stopped
       security_opt:
         - no-new-privileges:true
       cap_drop:
         - ALL
       cap_add:
         - CHOWN
         - SETGID
         - SETUID
       networks:
         - calculator_network
     
     nginx:
       image: nginx:alpine
       ports:
         - "80:80"
         - "443:443"
       volumes:
         - ./nginx.conf:/etc/nginx/nginx.conf:ro
         - nginx_logs:/var/log/nginx
       depends_on:
         - calculator
       restart: unless-stopped
       networks:
         - calculator_network
   
   volumes:
     calculator_logs:
     calculator_data:
     nginx_logs:
   
   networks:
     calculator_network:
       driver: bridge
   ```

4. Create `nginx.conf`:
   ```nginx
   events {
       worker_connections 1024;
   }
   
   http {
       upstream calculator {
           server calculator:8000;
       }
       
       # Rate limiting
       limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
       
       # Security headers
       add_header X-Frame-Options DENY;
       add_header X-Content-Type-Options nosniff;
       add_header X-XSS-Protection "1; mode=block";
       add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
       
       server {
           listen 80;
           server_name localhost;
           
           # Rate limiting
           limit_req zone=api burst=20 nodelay;
           
           # Proxy settings
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
           
           # Health check endpoint
           location /health {
               proxy_pass http://calculator;
               access_log off;
           }
           
           # API endpoints
           location / {
               proxy_pass http://calculator;
               
               # Timeouts
               proxy_connect_timeout 30s;
               proxy_send_timeout 30s;
               proxy_read_timeout 30s;
           }
           
           # Logging
           access_log /var/log/nginx/access.log;
           error_log /var/log/nginx/error.log;
       }
   }
   ```

### Task 2.2: Container Orchestration Scripts

1. Create `scripts/docker_build.sh`:
   ```bash
   #!/bin/bash
   set -e
   
   # Colors for output
   RED='\033[0;31m'
   GREEN='\033[0;32m'
   YELLOW='\033[1;33m'
   NC='\033[0m' # No Color
   
   echo -e "${GREEN}Building Calculator Docker Image${NC}"
   
   # Get version
   VERSION=$(python -c "from src.calculator.version import __version__; print(__version__)")
   echo -e "${YELLOW}Building version: $VERSION${NC}"
   
   # Build image
   echo -e "${YELLOW}Building Docker image...${NC}"
   docker build -t calculator-pro:$VERSION .
   docker tag calculator-pro:$VERSION calculator-pro:latest
   
   # Test image
   echo -e "${YELLOW}Testing Docker image...${NC}"
   docker run --rm calculator-pro:$VERSION calculator --version
   
   # Security scan
   if command -v trivy &> /dev/null; then
       echo -e "${YELLOW}Running security scan...${NC}"
       trivy image calculator-pro:$VERSION
   else
       echo -e "${YELLOW}Trivy not installed, skipping security scan${NC}"
   fi
   
   echo -e "${GREEN}Build completed successfully!${NC}"
   echo -e "Image: calculator-pro:$VERSION"
   ```

2. Create `scripts/deploy.sh`:
   ```bash
   #!/bin/bash
   set -e
   
   # Colors for output
   RED='\033[0;31m'
   GREEN='\033[0;32m'
   YELLOW='\033[1;33m'
   NC='\033[0m' # No Color
   
   # Configuration
   ENVIRONMENT=${1:-development}
   COMPOSE_FILE="docker-compose.yml"
   
   if [ "$ENVIRONMENT" = "production" ]; then
       COMPOSE_FILE="docker-compose.prod.yml"
   fi
   
   echo -e "${GREEN}Deploying Calculator to $ENVIRONMENT${NC}"
   
   # Pre-deployment checks
   echo -e "${YELLOW}Running pre-deployment checks...${NC}"
   
   # Check Docker is running
   if ! docker info > /dev/null 2>&1; then
       echo -e "${RED}Docker is not running${NC}"
       exit 1
   fi
   
   # Check compose file exists
   if [ ! -f "$COMPOSE_FILE" ]; then
       echo -e "${RED}Compose file $COMPOSE_FILE not found${NC}"
       exit 1
   fi
   
   # Validate compose file
   docker-compose -f "$COMPOSE_FILE" config > /dev/null
   
   # Build and deploy
   echo -e "${YELLOW}Building and starting services...${NC}"
   docker-compose -f "$COMPOSE_FILE" up --build -d
   
   # Wait for health checks
   echo -e "${YELLOW}Waiting for services to be healthy...${NC}"
   sleep 30
   
   # Test deployment
   echo -e "${YELLOW}Testing deployment...${NC}"
   
   # Test health endpoint
   if curl -f http://localhost/health > /dev/null 2>&1; then
       echo -e "${GREEN}Health check passed${NC}"
   else
       echo -e "${RED}Health check failed${NC}"
       docker-compose -f "$COMPOSE_FILE" logs
       exit 1
   fi
   
   # Test API endpoint
   if curl -f -X POST -H "Content-Type: application/json" \
        -d '{"operation": "add", "operands": [2, 3]}' \
        http://localhost/calculate > /dev/null 2>&1; then
       echo -e "${GREEN}API test passed${NC}"
   else
       echo -e "${RED}API test failed${NC}"
       exit 1
   fi
   
   echo -e "${GREEN}Deployment completed successfully!${NC}"
   echo -e "Services:"
   docker-compose -f "$COMPOSE_FILE" ps
   ```

## Part 3: Monitoring and Observability

### Task 3.1: Metrics and Health Checks

1. Create `src/calculator/monitoring.py`:
   ```python
   """Monitoring and metrics collection."""
   import time
   import psutil
   from typing import Dict, Any
   from functools import wraps
   
   from .logging_config import get_logger
   
   
   logger = get_logger('monitoring')
   
   
   class MetricsCollector:
       """Collect application metrics."""
       
       def __init__(self):
           self.start_time = time.time()
           self.operation_counts = {}
           self.operation_durations = {}
           self.errors = {}
   
       def record_operation(self, operation: str, duration: float, success: bool = True):
           """Record an operation metric."""
           if operation not in self.operation_counts:
               self.operation_counts[operation] = 0
               self.operation_durations[operation] = []
               self.errors[operation] = 0
           
           self.operation_counts[operation] += 1
           self.operation_durations[operation].append(duration)
           
           if not success:
               self.errors[operation] += 1
           
           logger.debug(f"Recorded {operation}: {duration:.4f}s, success={success}")
   
       def get_metrics(self) -> Dict[str, Any]:
           """Get current metrics."""
           uptime = time.time() - self.start_time
           
           # Calculate averages
           avg_durations = {}
           for op, durations in self.operation_durations.items():
               if durations:
                   avg_durations[op] = sum(durations) / len(durations)
               else:
                   avg_durations[op] = 0
           
           # System metrics
           memory_info = psutil.virtual_memory()
           cpu_percent = psutil.cpu_percent()
           
           return {
               'uptime_seconds': uptime,
               'system': {
                   'cpu_percent': cpu_percent,
                   'memory_percent': memory_info.percent,
                   'memory_used_mb': memory_info.used / (1024 * 1024),
                   'memory_available_mb': memory_info.available / (1024 * 1024)
               },
               'operations': {
                   'counts': self.operation_counts,
                   'average_duration_seconds': avg_durations,
                   'error_counts': self.errors
               }
           }
   
       def get_health_status(self) -> Dict[str, Any]:
           """Get health status."""
           try:
               metrics = self.get_metrics()
               
               # Health checks
               health_status = "healthy"
               issues = []
               
               # Check memory usage
               if metrics['system']['memory_percent'] > 90:
                   health_status = "unhealthy"
                   issues.append("High memory usage")
               
               # Check CPU usage
               if metrics['system']['cpu_percent'] > 90:
                   health_status = "unhealthy"
                   issues.append("High CPU usage")
               
               # Check error rates
               total_operations = sum(self.operation_counts.values())
               total_errors = sum(self.errors.values())
               
               if total_operations > 0:
                   error_rate = total_errors / total_operations
                   if error_rate > 0.1:  # 10% error rate
                       health_status = "unhealthy"
                       issues.append(f"High error rate: {error_rate:.2%}")
               
               return {
                   'status': health_status,
                   'timestamp': time.time(),
                   'uptime_seconds': metrics['uptime_seconds'],
                   'issues': issues
               }
               
           except Exception as e:
               logger.error(f"Health check failed: {e}")
               return {
                   'status': 'unhealthy',
                   'timestamp': time.time(),
                   'issues': [f"Health check error: {str(e)}"]
               }
   
   
   # Global metrics collector
   metrics_collector = MetricsCollector()
   
   
   def monitor_operation(operation_name: str):
       """Decorator to monitor operations."""
       def decorator(func):
           @wraps(func)
           def wrapper(*args, **kwargs):
               start_time = time.time()
               success = True
               
               try:
                   result = func(*args, **kwargs)
                   return result
               except Exception as e:
                   success = False
                   raise
               finally:
                   duration = time.time() - start_time
                   metrics_collector.record_operation(operation_name, duration, success)
           
           return wrapper
       return decorator
   ```

2. Update `src/calculator/calculator.py` to include monitoring:
   ```python
   # Add this import at the top
   from .monitoring import monitor_operation
   
   # Add decorators to methods
   class Calculator:
       # ... existing code ...
       
       @monitor_operation('add')
       def add(self, a: float, b: float) -> float:
           # ... existing implementation ...
       
       @monitor_operation('subtract')
       def subtract(self, a: float, b: float) -> float:
           # ... existing implementation ...
       
       @monitor_operation('multiply')
       def multiply(self, a: float, b: float) -> float:
           # ... existing implementation ...
       
       @monitor_operation('divide')
       def divide(self, a: float, b: float) -> float:
           # ... existing implementation ...
       
       @monitor_operation('sqrt')
       def square_root(self, x: float) -> float:
           # ... existing implementation ...
       
       @monitor_operation('power')
       def power(self, base: float, exponent: float) -> float:
           # ... existing implementation ...
   ```

### Task 3.2: Create Production Configuration

1. Create `docker-compose.prod.yml`:
   ```yaml
   version: '3.8'
   
   services:
     calculator:
       build: .
       environment:
         - ENVIRONMENT=production
         - DEBUG=false
         - LOG_LEVEL=INFO
         - CALC_PRECISION=10
         - LOG_FILE_PATH=/app/logs/calculator.log
       volumes:
         - calculator_logs:/app/logs
         - calculator_data:/app/data
       healthcheck:
         test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
         interval: 30s
         timeout: 3s
         retries: 3
         start_period: 40s
       restart: unless-stopped
       deploy:
         resources:
           limits:
             cpus: '0.5'
             memory: 512M
           reservations:
             cpus: '0.25'
             memory: 256M
       security_opt:
         - no-new-privileges:true
       cap_drop:
         - ALL
       cap_add:
         - CHOWN
         - SETGID
         - SETUID
       networks:
         - calculator_network
     
     nginx:
       image: nginx:alpine
       ports:
         - "80:80"
         - "443:443"
       volumes:
         - ./nginx.conf:/etc/nginx/nginx.conf:ro
         - nginx_logs:/var/log/nginx
       depends_on:
         - calculator
       restart: unless-stopped
       deploy:
         resources:
           limits:
             cpus: '0.25'
             memory: 128M
       networks:
         - calculator_network
     
     prometheus:
       image: prom/prometheus:latest
       ports:
         - "9090:9090"
       volumes:
         - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
         - prometheus_data:/prometheus
       command:
         - '--config.file=/etc/prometheus/prometheus.yml'
         - '--storage.tsdb.path=/prometheus'
         - '--web.console.libraries=/usr/share/prometheus/console_libraries'
         - '--web.console.templates=/usr/share/prometheus/consoles'
         - '--web.enable-lifecycle'
       restart: unless-stopped
       networks:
         - calculator_network
     
     grafana:
       image: grafana/grafana:latest
       ports:
         - "3000:3000"
       volumes:
         - grafana_data:/var/lib/grafana
       environment:
         - GF_SECURITY_ADMIN_PASSWORD=admin
       restart: unless-stopped
       networks:
         - calculator_network
   
   volumes:
     calculator_logs:
     calculator_data:
     nginx_logs:
     prometheus_data:
     grafana_data:
   
   networks:
     calculator_network:
       driver: bridge
   ```

## Part 4: Cloud Deployment

### Task 4.1: Kubernetes Deployment

1. Create `k8s/namespace.yaml`:
   ```yaml
   apiVersion: v1
   kind: Namespace
   metadata:
     name: calculator-prod
     labels:
       name: calculator-prod
   ```

2. Create `k8s/deployment.yaml`:
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: calculator-app
     namespace: calculator-prod
     labels:
       app: calculator
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: calculator
     template:
       metadata:
         labels:
           app: calculator
       spec:
         containers:
         - name: calculator
           image: calculator-pro:latest
           ports:
           - containerPort: 8000
           env:
           - name: ENVIRONMENT
             value: "production"
           - name: LOG_LEVEL
             value: "INFO"
           resources:
             requests:
               memory: "128Mi"
               cpu: "100m"
             limits:
               memory: "256Mi"
               cpu: "200m"
           livenessProbe:
             httpGet:
               path: /health
               port: 8000
             initialDelaySeconds: 30
             periodSeconds: 10
           readinessProbe:
             httpGet:
               path: /health
               port: 8000
             initialDelaySeconds: 5
             periodSeconds: 5
           securityContext:
             runAsNonRoot: true
             runAsUser: 1000
             allowPrivilegeEscalation: false
             capabilities:
               drop:
               - ALL
   ```

3. Create `k8s/service.yaml`:
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: calculator-service
     namespace: calculator-prod
   spec:
     selector:
       app: calculator
     ports:
     - protocol: TCP
       port: 80
       targetPort: 8000
     type: ClusterIP
   ```

4. Create `k8s/ingress.yaml`:
   ```yaml
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
     name: calculator-ingress
     namespace: calculator-prod
     annotations:
       nginx.ingress.kubernetes.io/rate-limit: "100"
       nginx.ingress.kubernetes.io/rate-limit-window: "1m"
   spec:
     rules:
     - host: calculator.example.com
       http:
         paths:
         - path: /
           pathType: Prefix
           backend:
             service:
               name: calculator-service
               port:
                 number: 80
   ```

### Task 4.2: Cloud Deployment Scripts

1. Create `scripts/deploy_cloud.sh`:
   ```bash
   #!/bin/bash
   set -e
   
   # Configuration
   CLOUD_PROVIDER=${1:-aws}
   ENVIRONMENT=${2:-production}
   
   echo "Deploying to $CLOUD_PROVIDER ($ENVIRONMENT)"
   
   case $CLOUD_PROVIDER in
       "aws")
           echo "Deploying to AWS ECS..."
           # Add AWS ECS deployment logic
           ;;
       "gcp")
           echo "Deploying to Google Cloud Run..."
           # Add GCP Cloud Run deployment logic
           ;;
       "azure")
           echo "Deploying to Azure Container Instances..."
           # Add Azure deployment logic
           ;;
       "k8s")
           echo "Deploying to Kubernetes..."
           kubectl apply -f k8s/
           ;;
       *)
           echo "Unknown cloud provider: $CLOUD_PROVIDER"
           exit 1
           ;;
   esac
   
   echo "Deployment completed!"
   ```

## Part 5: Testing and Validation

### Task 5.1: Integration Tests

1. Create `tests/test_integration.py`:
   ```python
   """Integration tests for the calculator application."""
   import subprocess
   import time
   import requests
   import pytest
   from pathlib import Path
   
   
   @pytest.fixture(scope="module")
   def docker_service():
       """Start and stop Docker service for testing."""
       # Start service
       subprocess.run(["docker-compose", "up", "-d"], check=True)
       
       # Wait for service to be ready
       for _ in range(30):
           try:
               response = requests.get("http://localhost/health", timeout=1)
               if response.status_code == 200:
                   break
           except requests.exceptions.RequestException:
               pass
           time.sleep(1)
       
       yield
       
       # Stop service
       subprocess.run(["docker-compose", "down"], check=True)
   
   
   def test_health_endpoint(docker_service):
       """Test health endpoint."""
       response = requests.get("http://localhost/health")
       assert response.status_code == 200
       data = response.json()
       assert data["status"] == "healthy"
   
   
   def test_calculation_api(docker_service):
       """Test calculation API."""
       response = requests.post(
           "http://localhost/calculate",
           json={"operation": "add", "operands": [5, 3]}
       )
       assert response.status_code == 200
       data = response.json()
       assert data["result"] == 8.0
   
   
   def test_cli_commands():
       """Test CLI commands."""
       # Test basic command
       result = subprocess.run(
           ["calculator", "add", "5", "3"],
           capture_output=True,
           text=True
       )
       assert result.returncode == 0
       assert "8" in result.stdout
       
       # Test version
       result = subprocess.run(
           ["calculator", "--version"],
           capture_output=True,
           text=True
       )
       assert result.returncode == 0
       assert "calculator" in result.stdout
   
   
   def test_batch_processing():
       """Test batch processing."""
       # Create test batch file
       batch_content = """add 5 3
   multiply 2 4
   sqrt 16
   """
       batch_file = Path("/tmp/test_batch.txt")
       batch_file.write_text(batch_content)
       
       try:
           result = subprocess.run(
               ["calculator", "batch", str(batch_file)],
               capture_output=True,
               text=True
           )
           assert result.returncode == 0
           # Should contain results for all operations
           assert "8" in result.stdout  # 5 + 3
           assert "8" in result.stdout  # 2 * 4
           assert "4" in result.stdout  # sqrt(16)
       finally:
           batch_file.unlink(missing_ok=True)
   ```

### Task 5.2: Performance Tests

1. Create `tests/test_performance.py`:
   ```python
   """Performance tests for the calculator."""
   import time
   import concurrent.futures
   import requests
   import pytest
   
   from calculator import Calculator
   
   
   def test_calculation_performance():
       """Test calculation performance."""
       calc = Calculator()
       
       # Measure single operation
       start_time = time.time()
       for _ in range(1000):
           calc.add(1, 2)
       duration = time.time() - start_time
       
       # Should complete 1000 operations in less than 1 second
       assert duration < 1.0
       
       # Calculate operations per second
       ops_per_second = 1000 / duration
       print(f"Operations per second: {ops_per_second:.2f}")
       
       # Should handle at least 10,000 ops/second
       assert ops_per_second > 10000
   
   
   def test_memory_usage():
       """Test memory usage during operations."""
       import psutil
       import os
       
       process = psutil.Process(os.getpid())
       initial_memory = process.memory_info().rss / (1024 * 1024)  # MB
       
       calc = Calculator()
       
       # Perform many operations
       for i in range(10000):
           calc.add(i, i + 1)
       
       final_memory = process.memory_info().rss / (1024 * 1024)  # MB
       memory_increase = final_memory - initial_memory
       
       print(f"Memory increase: {memory_increase:.2f} MB")
       
       # Memory increase should be reasonable (less than 50MB)
       assert memory_increase < 50
   
   
   @pytest.mark.skipif(not pytest.config.getoption("--integration"),
                       reason="Need --integration option to run")
   def test_api_load():
       """Test API under load."""
       def make_request():
           response = requests.post(
               "http://localhost/calculate",
               json={"operation": "add", "operands": [1, 2]},
               timeout=5
           )
           return response.status_code == 200
       
       # Test with concurrent requests
       with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
           futures = [executor.submit(make_request) for _ in range(100)]
           results = [future.result() for future in futures]
       
       # All requests should succeed
       success_rate = sum(results) / len(results)
       assert success_rate > 0.95  # At least 95% success rate
   ```

## Common Pitfalls

- **Container security**: Always run containers as non-root users
- **Resource limits**: Set appropriate CPU and memory limits
- **Health checks**: Implement proper health and readiness checks
- **Logging**: Structure logs for easy parsing and monitoring
- **Secrets**: Never embed secrets in container images
- **Performance**: Monitor and optimize for production loads

## What Success Looks Like

By the end of this assignment, you should have:
- A production-ready CLI application with advanced features
- Containerized application with proper security practices
- Monitoring and observability implementation
- Cloud deployment configuration
- Comprehensive testing including integration and performance tests
- Complete CI/CD pipeline for automated deployment

## Self-Assessment Questions

1. How do containerization practices improve application deployment?
2. What monitoring metrics are most important for production applications?
3. How does infrastructure as code benefit development teams?
4. What security considerations are critical for production deployments?
5. How do you balance application performance with resource constraints?

## Submission Requirements

Submit the following:

1. Your complete production-ready calculator application
2. Working Docker containers with successful health checks
3. Evidence of successful deployment (screenshots/logs)
4. Performance test results
5. A final reflection document (500-700 words) addressing:
   - How this project demonstrates professional Python development practices
   - The evolution from simple scripts to production-ready applications
   - Key learnings about software deployment and operations
   - How these skills apply to real-world software development

## Additional Resources

- [Click Documentation](https://click.palletsprojects.com/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [The Twelve-Factor App](https://12factor.net/)
- [Prometheus Monitoring](https://prometheus.io/docs/)
- [Container Security Best Practices](https://sysdig.com/blog/dockerfile-best-practices/)

````