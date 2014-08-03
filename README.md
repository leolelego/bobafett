Boba Fett Theme For Jekyll
==========================

Boba Fett Theme is a theme/template for [Jekyll](http://jekyllrb.com) makes your **resume** such as Boba Fett

![screen]()

## How to use it

### General informations

There is three files to customize your site : 

- ` _config.yml` for customizing your **informations** (name, summary, twitter, linkedin...),
- `_less/bobafett.less` for customizing the **desgin** (fonts, colors, sizes...),
- `CNAME` for your custom domain.

All sections in the resume are fill with your **markdown** post in `_posts` 
 
### Quick start

#### get it :

- download **[sources file](https://github.com/leoderbois/Boba-Fett-Theme-For-Jekyll/archive/master.zip)** or **clone**, customize it and run Jekyll on your server,
- [**Fork the master branch**](https://github.com/leoderbois/Boba-Fett-Theme-For-Jekyll/fork) to a new project of your github (best choice). And *Pull* it on your computer.

#### Customize

- customize `_config.yml`with your informations,
- customize `_less/bobafett.less`,
- compile the `_less/main.less` file ([doc here](http://lesscss.org/)), *personnaly i use [Codekit on OSX](https://incident57.com/codekit/)*,
- or if you don't want to use `.less` change the `css/main.css`.

#### Start your server

- intstall Jekyll : [jekyllrb.com](http://jekyllrb.com/) if needed,
- go to the folder where is your resume/theme with your **terminal**,
- launch command : `jekyll serve -w --baseurl ''`,
- Go to [http://localhost:4000](http://localhost:4000).



## Exemples of site using this template

- [Boba Fett Resume](http://bobafett.leoderbois.com)
- [Léo Derbois resume](http://www.leoderbois.com)

> tell me if you use my theme :) 


## Development

#### There is 2 statics branches :

- Master for the *releases* version,
- gh-pages for the [demo](http://bobafett.leoderbois.com),

and branches for fixes and developments.


#### This project use **Frameworks** : 

- [Jekyll](http://jekyllrb.com) 
- [Boostrap](http://getbootstrap.com)
- [less](http://lesscss.org)
- [Font Awesome](http://fortawesome.github.io/Font-Awesome/)

## Todo

- scroll animaton href# in nav (in JS) *need help !*
- min-height nav

**[Contact me](mailto:contact@leoderbois.com) if you have ideas !**

## License

Open sourced under the [MIT license](/LICENSE.md).


