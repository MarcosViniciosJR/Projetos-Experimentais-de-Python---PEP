# Changelog

Todas as atualizações e mudanças notáveis deste projeto serão documentadas neste arquivo.

## [0.1.0] - 20/11/2026 20:52
Criação e reformulação da estrutura inicial do sistema acadêmico, menu interativo e documentação base.

### Adicionado
- `menu_cad_ti.py`:
  - Estrutura base do menu interativo no terminal (opções 0 a 9).
  - Base de dados inicial em memória com 20 alunos de TI.
- `jr_lab_ti.py`:
  - Criação do módulo reservado para funções de cálculo, validação e regras de negócio.
- `README.md` & `CHANGELOG.md`:
  - Documentação inicial do projeto e histórico de versões.

<!-- 
====================================================================
COLA RÁPIDA DE ATUALIZAÇÃO (Invisível no GitHub - Copie e cole acima)
====================================================================

## [X.Y.Z] - DD/MM/AAAA HH:MM
### Adicionado
- `jr_lab_ti.py`:
  - 
- `menu_cad_ti.py`:
  - 

### Alterado
- `jr_lab_ti.py`:
  - 

### Corrigido
- `menu_cad_ti.py`:
  - 

====================================================================
COMANDOS BÁSICOS DO GIT (Fluxo de envio para o GitHub)
====================================================================
1. Conferir o que foi alterado:
   git status

2. Preparar os arquivos para salvar:
   git add .

3. Registrar a versão localmente (use o prefixo certo):
   git commit -m "feat: descrição da nova funcionalidade (vX.Y.Z)"
   (Outros prefixos: "fix:" para correção | "docs:" para README/Changelog)

4. Enviar as alterações para o GitHub:
   git push

====================================================================
GERAR EXECUTÁVEL (.EXE) COM PYINSTALLER (Windows PowerShell/Terminal)
====================================================================
0. Instalar o PyInstaller (apenas na primeira vez):
   pip install pyinstaller

1. Limpar o .exe e pastas temporárias da versão anterior:
   Remove-Item -Recurse -Force build, dist, *.spec -ErrorAction SilentlyContinue

2. Gerar um novo .exe único (o arquivo final fica dentro da pasta "dist"):
   pyinstaller --onefile --clean menu_cad_ti.py

   (Opcional - se quiser salvar com o número da versão no nome):
   pyinstaller --onefile --clean --name "menu_cad_ti_v0.1.0" menu_cad_ti.py
====================================================================
-->