# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'file://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Default monospace fonts. Whenever "monospace" is used in a font
# setting, it's replaced with the fonts listed here.
# Type: Font
c.fonts.monospace = '"DejaVu Sans Mono", "xos4 Terminus", Terminus, Monospace, Monaco, "Bitstream Vera Sans Mono", "Andale Mono", "Courier New", Courier, "Liberation Mono", monospace, Fixed, Consolas, Terminal'

config.bind('j', 'scroll-page 0 0.3')
config.bind('k', 'scroll-page 0 -0.3')

config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')

config.bind('cr', 'tab-only -p')
config.bind('cl', 'tab-only -n')

config.bind(',y', 'hint links spawn -d st -e youtube-dl {hint-url}')
config.bind(',m', 'hint links spawn -d mpv {hint-url}')

config.bind('<Ctrl+Shift+j>', 'scroll-page 0 0.9')
config.bind('<Ctrl+Shift+k>', 'scroll-page 0 -0.9')