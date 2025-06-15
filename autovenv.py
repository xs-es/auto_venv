# Prompt user for the name of the virtual environment
$venvName = Read-Host "What would you like to name your virtual environment? (default: venv)"
if ([string]::IsNullOrWhiteSpace($venvName)) {
    $venvName = "venv"
}

# Check if Python is available
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "❌ Python is not installed or not in PATH."
    exit 1
}

# Create the virtual environment
Write-Host "Creating virtual environment '$venvName'..."
python -m venv $venvName

# Define activation script path
$activateScript = Join-Path $venvName "Scripts\Activate.ps1"

# Validate activation script exists
if (-not (Test-Path $activateScript)) {
    Write-Error "❌ Activation script not found. Something went wrong with the venv creation."
    exit 1
}

# Activate and upgrade pip-related tools in a new PowerShell session
Write-Host "Activating '$venvName' and upgrading pip, setuptools, and wheel..."
powershell -NoExit -Command @"
`& `"$activateScript`"
python -m pip install --upgrade pip setuptools wheel
"@
