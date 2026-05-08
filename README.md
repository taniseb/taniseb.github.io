# taniseb.github.io — Portfolio Site

Quarto website. Deploy via GitHub Pages.

## Setup (uma vez só)

```bash
# 1. Instalar Quarto: https://quarto.org/docs/get-started/
# 2. Instalar dependências Python
pip install jupyter

# 3. Clonar / inicializar o repo
git init
git remote add origin https://github.com/taniseb/taniseb.github.io.git
```

## Rodar localmente

```bash
quarto preview
# Abre em http://localhost:4848
```

## Publicar no GitHub Pages

```bash
# Gera o site na pasta /docs
quarto render

# Sobe para o GitHub
git add .
git commit -m "update site"
git push origin main
```

Depois: no GitHub → Settings → Pages → Branch: main, Folder: /docs → Save.
O site fica em https://taniseb.github.io em ~2 minutos.

## Adicionar um novo projeto

1. Criar arquivo em `projects/nome-do-projeto.qmd`
2. Copiar o template de `projects/nowcasting.qmd`
3. Adicionar card em `projects/index.qmd` e `index.qmd`
4. `quarto render` + `git push`

## Estrutura

```
portfolio-site/
├── _quarto.yml          # configuração do site
├── index.qmd            # homepage
├── about.qmd            # bio
├── styles.css           # estilo
├── projects/
│   ├── index.qmd        # lista de projetos
│   └── nowcasting.qmd   # projeto 1 (template)
└── docs/                # gerado pelo quarto render (não editar)
```

## TODO antes de publicar

- [ ] Atualizar LinkedIn URL em `_quarto.yml` e `about.qmd`
- [ ] Adicionar foto em `assets/foto.jpg` e referenciar no `about.qmd`
- [ ] Criar repo `taniseb.github.io` no GitHub
- [ ] Criar repo separado `nowcasting-ipca` para o código do projeto 1
