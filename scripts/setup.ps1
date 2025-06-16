# Set initial Python executable
$PYTHON = "python"

# Check if 'python' is available
if (-not (Get-Command $PYTHON -ErrorAction SilentlyContinue)) {
    $PYTHON = "python3"
}

# Check if the chosen Python is available
if (-not (Get-Command $PYTHON -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed on this system."
    exit 1
}

# Create virtual environment
& $PYTHON -m venv env

# Activate virtual environment
$envScript = ".\env\Scripts\Activate.ps1"
if (-Not (Test-Path $envScript)) {
    Write-Host "Failed to find the virtual environment activation script."
    exit 1
}
. $envScript

# Install dependencies
& $PYTHON -m pip install -r requirements.txt
