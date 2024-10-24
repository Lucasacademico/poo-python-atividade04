$exclude = @("venv", "bot-formulario-atividade04.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot-formulario-atividade04.zip" -Force