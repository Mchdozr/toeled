# Toeled Theme Tokens

Static HTML + Layui + UIkit + vanilla CSS (`layout.css`, `style.css`). No CSS variables, no Tailwind. Colors are hardcoded.

## Compact token summary

### Color
| Token | Value | Use |
|---|---|---|
| Brand navy | `#112698` | titles, CTA fill, header accent, gradients |
| Brand navy deep | `#001584` | CTA gradient, hero overlays |
| Accent red | `#ee1d23` | alerts / emphasis |
| Accent orange | `#d96515` | secondary highlights |
| Text primary | `#171717` / `#151515` | body |
| Text muted | `#333` / `#595959` / `#666` | captions |
| Surface | `#fff` | cards, header |
| Surface gray | `#f6f6f6` / `#f2f2f2` / `#f1f1f3` | header top, sections |
| Link hover | `#0762d5` | float widgets |

Gradient CTA: `linear-gradient(75deg, #112698 0%, #001584 51%, #112698 100%)`

### Typography
- Font: `'Microsoft YaHei', Arial, sans-serif`
- H1 `.public-title`: 42px bold, `#112698`, centered
- Nav: ~16px, dark on white (scrolled) / light on transparent (hero)
- Body: 14–16px, `#333`

### Spacing & layout
- Content max: `.mauto` 1600px
- Header logo height: 132px
- Section padding: ~0.7–1rem (rem-based from plugin.css)
- Breakpoints: 767px mobile (`.header-m` shown, desktop `.header` hidden)

### Radius & motion
- CTA `.contact-btn`: 23px pill, 180×45px, navy fill, white text
- Inputs: bottom-border / rounded 20px on floating form
- Hover image scale: 1.1 over 0.8s
- Header transition: 0.5s
- `hsm="fadeup"` scroll reveals

### Logo
- Dark header: `/public/wwwroot/images/logo.svg` (white "TOELED" wordmark)
- Light/mobile: `/public/wwwroot/images/logo10.svg` (black "TOELED" wordmark)

## Raw source (key rules)

```css
/* layout.css excerpts */
.mauto { max-width: 1600px }
header { position: fixed; z-index: 555; left: 0; top: 0; width: 100%; }
.logo { height: 132px; display: flex; align-items: center; }
.public-title { font-weight: bold; font-size: 42px; color: #112698; text-align: center; }
.contact-btn {
  max-width: 180px; width: 100%; height: 45px;
  background: #112698; border-radius: 23px;
  display: flex; align-items: center; justify-content: center;
  font-size: 16px; color: #FFFFFF; margin: auto; margin-top: 20px;
}
```

```css
/* style.css excerpts */
.home-model1 { background-image: url("../images/home_18.png"); background-size: cover; }
/* navy fills #112698, deep #001584, orange #d96515 */
```
