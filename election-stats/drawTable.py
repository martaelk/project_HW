from rich.console import Console
from rich.table import Table

def drawTable(title, header, rows):
    table = Table(show_header=True, header_style="bold cyan", border_style="bright_yellow", show_lines=True)

    # Add headers to the table
    for column in header:
        table.add_column(column)

    # Add rows to the table
    for row in rows:
        table.add_row(*row, style='bright_green')

    console = Console()
    console.print(title, style="bold magenta")
    console.print(table)