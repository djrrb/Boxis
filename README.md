# Boxis

Boxis (box + axis) is an OpenType Variable font designed for testing OpenType Variable fonts. 

You can use it to create a visual difference between browsers that support variable fonts and browsers that do not. Visit the [test page](http://stuff.djr.com/boxis) to see it in action!

This demo was made by [David Jonathan Ross](https://djr.com). Thanks to [Alexandre Saumier Demers](http://asaumierdemers.com) for his help figuring out how to position the default style.

## Axes

Boxis currently has four axes:

* wdth: The width of the box (0 - 1000, 750 default)
* hght: The height of the box (0 - 1000, 750 default)
* trac: The space on either side of the box (0 - 1000, 0 default)
* desc: Move the bottom of the box from the font baseline to the descent (0 - 250, 0 default)

## Notes

The axis values roughly correspond to 1000-per-em units. So the ascent (hght) is 750, the descent (desc) is 250, totalling 1000. However I’ve left the option of letting the box exceed the ascent, so you can also get a 1000×1000 box that sits on the baseline.

fontmake uses cu2qu to handle the outlines in the font, and it doesn’t seem to like points overlapping each other the way I’ve drawn them. I think it’s possible to do this, but for now the zero masters are actually one unit thick instead of zero.