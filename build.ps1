$ErrorActionPreference = "Stop"
Push-Location $PSScriptRoot
try {
    $pythonRpg = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
    if (-not (Test-Path -LiteralPath $pythonRpg)) {
        throw "Crie .venv e instale requirements-dev.txt antes de gerar o executavel."
    }
    & $pythonRpg -m pytest -q
    if ($LASTEXITCODE -ne 0) { throw "Os testes falharam." }
    & $pythonRpg -m PyInstaller --noconfirm --clean --onefile --windowed --name OOP_RPG_Game --add-data "src/artes:artes" src/main.py
    if ($LASTEXITCODE -ne 0) { throw "Falha ao gerar o executavel." }
    Write-Output "Executavel: dist\OOP_RPG_Game.exe"
}
finally {
    Pop-Location
}
