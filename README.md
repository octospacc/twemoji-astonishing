# 🌈 Twemoji Astonishing 😲

Like **Font-Awesome, but for [Twitter Emojis](https://github.com/twitter/twemoji)** - and this time, it's **astonishing**! 😄

![Banner with some emojis](Banner.png)

Modern **drop-in replacement** for projects like [Twemoji-Amazing](https://github.com/SebastianAigner/twemoji-amazing), with some **quality-of-life improvements**:

- Easy support for **fallback text** emojis
- Literal **emojis as CSS class names**, in addition to text names

## Usage

### CSS Variants

You can get your preferred variant of the CSS file for use in your webpages:

- `twemoji-astonishing`: The **full package** with all the features
- `twemoji-astonishing.chars`: **Only literal emojis** used as class names
- `twemoji-astonishing.names`: **Only ASCII names** used as class names, like Twemoji-Amazing

Every variant, of course, has both a **pure** (`.css`) version, and a **minified** (`.min.css`) one.

### Getting the Files

For getting the files and using them, you can choose between:

- **Hotlinking** to the latest file hosted on the Pages branch of the repo:
  - **Directly**: `https://octtspacc.gitlab.io/twemoji-astonishing/maxcdn/<VARIANT>.css`
  - (Better) **Using a CDN** like jsDelivr: `https://cdn.jsdelivr.net/gh/octospacc/twemoji-astonishing@gh-pages/<VARIANT>.css`

- **Downloading a prebuilt archive** containing all the CSS and SVG files, which you can host on your own server:
  - See file listing [here (GitLab)](https://octtspacc.gitlab.io/twemoji-astonishing/index.html), or [here (GitHub)](https://octospacc.github.io/twemoji-astonishing/index.html); archives are in the "Archives" directory.

### Using the CSS Classes

Just **assign** the **base class** (`twa`), an **emoji class**, and optionally any option class **to a new inline element**.

#### Size Option Classes

Like for Font-Awesome and Twemoji-Amazing, the following classes can be used to **alter emoji sizes**:  
`twa-lg`, `twa-2x`, `twa-3x`, `twa-4x`, `twa-5x`.

#### Emoji classes

Emoji classes can be used in one of 2 forms.

First, an emoji class can be the **standard form** `twa-emoji-name`; essentially, the ASCII name of the emoji, prefixed by `twa-`.  
Example:  
```html
<span class="twa twa-astonished-face"></span>
```

You can also (additionally, or exclusively) use **literal emojis** (always prefixed by `twa-`) as class names.
Example:  
```html
<span class="twa twa-🗿"></span>
```

Any text inside elements with the `twa` class will be properly hidden via CSS.  
This means that you are free to write text inside those HTML tags - including emoji characters, that will act as a **fallback on unsupported platforms** (very old browsers), while also **allowing emojis to be copied** with other text when that gets selected. In fact, you should do this.  
Example:  
```html
<span class="twa twa-exploding-head">🤯</span>
```

### Finding emojis

- You can **look for emoji names, codes, and characters** at [Emoji List](https://unicode.org/emoji/charts/emoji-list.html) by the Unicode Consortium. The names you get from the table correspond to the CSS class names if you remove letter accents, remove special characters, and replace spaces with dashes.

- [Emojipedia](https://emojipedia.org) is also a **great resource** for finding emoji information - the above, but also much more. For each emoji on the site, the URL names correspond to the CSS class names.

## Building

Running `./Tools/BuildCSS.py` **generates** all final **CSS files**. (Requires Python >= 3.9).

`./Tools/DeployPages.sh` also **does other tasks**, like downloading a fresh copy of Twemoji SVG files and creating archives.

## Credits and Licenses

**License for Twemoji-Astonishing** scripts, snippets, and documentation: [MIT](https://mit-license.org).

Uses CSS snippets from [Twemoji-Amazing](https://github.com/SebastianAigner/twemoji-amazing), licensed under [MIT](https://mit-license.org).

The project exists solely on top of [Twemoji](https://twemoji.twitter.com). Their graphics are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0). Please adhere to the [Twemoji attribution requirements](https://github.com/twitter/twemoji#attribution-requirements) when using these emojis.

The included tools for building the CSS files scrape the latest version of the [emoji-test.txt](https://unicode.org/Public/emoji/) list from the Unicode Consortium. See that for copyright and licensing.
