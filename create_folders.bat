:: In your main project directory (e.g., portfolio_dashboard)

:: 1. Create all the necessary directories.
:: The 'mkdir' command can create nested subdirectories at once.
ECHO Creating project directories...
mkdir "src\models"
mkdir "src\components\charts"
mkdir "src\components\tables"
mkdir "src\views"
mkdir "tests"

:: 2. Create all the empty files.
:: The 'type nul > [filename]' command is the standard CMD way to create an empty file.
ECHO Creating project files...
type nul > "src\__init__.py"
type nul > "src\models\__init__.py"
type nul > "src\components\__init__.py"
type nul > "src\components\charts\__init__.py"
type nul > "src\components\tables\__init__.py"
type nul > "src\views\__init__.py"

type nul > "src\app.py"
type nul > "src\state.py"
type nul > "src\models\factory.py"
type nul > "src\components\charts\performance.py"
type nul > "src\views\fund_overview.py"
type nul > "src\views\portfolio_level.py"

ECHO Project structure created successfully.