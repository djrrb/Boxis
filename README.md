# Boxis

Boxis (box + axis) is an OpenType Variable font designed for testing OpenType Variable fonts. You can use it to create dummy text that will not appear in browsers that do not support [OpenType Font Variations](https://www.microsoft.com/en-us/Typography/OpenTypeSpecification.aspx).

## Axes

Boxis currently has four axes:

* wdth: The width of the box (0 - 1000)
* hght: The height of the box (0 - 1000, 750 cap height)
* trac: The space on either side of the box (0 - 1000)
* desc: Move the bottom of the box from the font baseline to the descent (0 - 250)

## Notes

The default style is almost invisible, which should create a jarring difference between browsers that support variable fonts and those that don’t.

The axis values roughly correspond to 1000-per-em units. So the ascent (hght) is 750, the descent (desc) is 250, totalling 1000. However I’ve left the option of letting the box exceed the ascent, so you can get a 1000x1000 box that sits on the baseline.

fontmake uses cu2qu to handle the outlines in the font, and it doesn’t seem to like points overlapping each other the way I’ve drawn them. I’ve tried both directions. I think it’s possible to do this, and am not sure what’s up. For now these are actually one unit wide instead of zero, which is why the default style is not totally invisible.