# POuL reveal.js template

This is the `reveal.js` slides template for all POuL lessons.

It is mandatory for new courses to either use this or the Beamer base template.

## Important - Slides versioning

Slides repositories should be placed under the appropriate suborganization, under
[/corsi](https://gitlab.poul.org/corsi).

All years slides should be **in the same repo**, even if they use different
technologies. Use a branch `revealjs`/`beamer` to distinguish the two trees.

All years slides must be tagged appropriately:

```bash
git tag -m 2019 2019
```

If you need to move a tag, add `--force`. You might need to ask a sysadmin if you
need to force-push.

## Getting Started

In order for the slides to work (ie. display anything) you need to run:
`git submodule update --init`

In case you need the mathjax submodule as well
`git submodule update --init --recursive`

You can add `--depth 1` to the previous commands to improve the update speed but only if you are using the latest `reveal.js` module.

## How do I use this thing?

### Where do I write my stuff?

1. Create a new repo into the appropriate sub-organization
1. Clone this repo
1. Change origin to your repo
1. Push
1. Add author's info in `./slides/intro.html` and `./slides/outro.html`
1. Put your content in `./slides/content.md` or add slides files in `./slides/` and link these in `./index.html`

All user-supplied content MUST be placed under the `slides` directory.

This allows to easily merge changes from this template without breaking the
slides.

If you're updating old slides you should resolve all the conflicts yourself and
migrate to the new layout described here.

### How do I write my stuff?

Using Vim.

[Here][markdown-guide] you can find a comprehensive guide to the Markdown syntax.

Remember to use three dashes (`---`) to create a new slide horizontally and
four dashes (`----`) to create a new one vertically.

Use `Notes:` to add reader notes to your slide.

Alternatively you can write your slides with pure **html**

### How do I see my stuff?

You can run `./deploy.py` with Python 3 and open the provided link in your browser.

## How do I make a PDF out of the slides?

Click on the printer symbol in the bottom-left corner to get the printable version of the slides.

Then just use the print function of your browser to make a PDF of the page.

On **Chrome/ium** make sure you **scroll to the top** of your slides before printing,
otherwise, for whatever reason, the background of the slides will be borked.

On **Firefox** it is advised to enable *Print Backgrounds* under the *Options* tab,
to select paper size *Choukei 2 Envelope* and *Landscape* orientation.

[download]: https://gitlab.poul.org/corsi/revealjs-poul/repository/archive.zip?ref=master
[markdown-guide]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

## GitLab Pages slides preview

It is possible to use GitLab Pages to preview the slides in order to send them for review
to the mailing list.

#### Important
GitLab Pages **must not** be used to actually publish the slides, and links to it
**must not** be given to course attendants. Use [slides.poul.org](https://slides.poul.org)
instead.


A `.gitlab-ci.yml` config is provided in this template. It simply copies the whole
`master` branch of the repo to the Pages website.

To use it:

- Enable CI for your repository:
  - Go to `Settings` > `General` > `Visibility`
  - Enable `Pipelines` under the `Repository` section

A CI build job for the `master` branch should run automatically. If it doesn't, go to
`CI / CD` and click `Run Pipeline`.

You can find the link to your Pages preview under `Settings` > `Pages`.

## License selection
By deafault this template indicates the license as CC-BY-SA, however by editing
the `slides/outro.html` file one can pick a different license from the "suggested"
ones.  
(This however does not forbid anyone from using a different license altogether,
just that those are the ones that we find suit best `;)` )
