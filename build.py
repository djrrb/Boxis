import os
axes = {
    #name: (x, y, w, h)
    'origin': ( (0, 0, 1, 1, 0), 0, None),
    #'default': ( (0, 0, 750, 750, 750), 750, None),
    'wdth': ( (0, 0, 1000, 1, 1000), 1000, 'Width'),
    'hght': ( (0, 0, 1, 1000, 0), 1000, 'Height'),
    'desc': ( (0, -250, 1, 250, 0), 250, 'Descender'),
    'trac': ( (500, 0, 1, 1, 1000), 1000, 'Tracking'),
    }
    

series = 'Boxis'
elementName = 'uni2588'
destBase = os.path.join(os.path.split(__file__)[0], 'sources')

ds = """<?xml version='1.0' encoding='utf-8'?>
<designspace format="3">
    <axes>"""
    
for axis, values in axes.items():
    if axis != 'origin':
        ds += """
        <axis default="0" maximum="%s" minimum="0.0" name="%s" tag="%s" />""" %(values[1], axis, axis)
    
ds += """
    </axes>
    <sources>"""

for axis, values in axes.items():
    boxDimensions, axisValue, axisTitle = values
    x, y, w, h, sw = boxDimensions
    if axisValue:
        styleName = axis+str(axisValue)
    else:
        styleName = 'Regular'
        
    sourceName = series + '-' + styleName
    fileName = sourceName + '.ufo'
    path = os.path.join(destBase, fileName)
    f = NewFont(showUI=False)
    g = f.newGlyph(elementName)
    p = g.getPen()
    p.moveTo((x, y))
    p.lineTo((x+w, y))
    p.lineTo((x+w, y+h))
    p.lineTo((x, y+h))
    p.lineTo((x, y))
    p.closePath()
    g.width = sw
    f.info.familyName = series
    f.info.styleName = styleName
    f.info.openTypeNameDesigner = 'David Jonathan Ross'
    f.info.openTypeNameDesignerURL = 'http://www.djr.com'
    f.info.openTypeNameManufacturer = 'David Jonathan Ross'
    f.info.openTypeNameManufacturerURL = 'http://www.djr.com'
    f.info.copyright = '(C) David Jonathan Ross 2017'
    
    f.lib["public.glyphOrder"] = ['space', 'exclam', 'quotedbl', 'numbersign', 'dollar', 'percent', 'ampersand', 'quotesingle', 'parenleft', 'parenright', 'asterisk', 'plus', 'comma', 'hyphen', 'period', 'slash', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'colon', 'semicolon', 'less', 'equal', 'greater', 'question', 'at', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'bracketleft', 'backslash', 'bracketright', 'asciicircum', 'underscore', 'grave', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'braceleft', 'bar', 'braceright', 'asciitilde', 'exclamdown', 'cent', 'sterling', 'currency', 'yen', 'brokenbar', 'section', 'dieresis', 'copyright', 'ordfeminine', 'guillemotleft', 'logicalnot', 'registered', 'macron', 'degree', 'plusminus', 'two.sups', 'three.sups', 'acute', 'mu1', 'paragraph', 'periodcentered', 'cedilla', 'one.sups', 'ordmasculine', 'guillemotright', 'onequarter', 'onehalf', 'threequarters', 'questiondown', 'Agrave', 'Aacute', 'Acircumflex', 'Atilde', 'Adieresis', 'Aring', 'AE', 'Ccedilla', 'Egrave', 'Eacute', 'Ecircumflex', 'Edieresis', 'Igrave', 'Iacute', 'Icircumflex', 'Idieresis', 'Eth', 'Ntilde', 'Ograve', 'Oacute', 'Ocircumflex', 'Otilde', 'Odieresis', 'multiply', 'Oslash', 'Ugrave', 'Uacute', 'Ucircumflex', 'Udieresis', 'Yacute', 'Thorn', 'germandbls', 'agrave', 'aacute', 'acircumflex', 'atilde', 'adieresis', 'aring', 'ae', 'ccedilla', 'egrave', 'eacute', 'ecircumflex', 'edieresis', 'igrave', 'iacute', 'icircumflex', 'idieresis', 'eth', 'ntilde', 'ograve', 'oacute', 'ocircumflex', 'otilde', 'odieresis', 'divide', 'oslash', 'ugrave', 'uacute', 'ucircumflex', 'udieresis', 'yacute', 'thorn', 'ydieresis', 'dotlessi', 'Lslash', 'lslash', 'OE', 'oe', 'Scaron', 'scaron', 'Ydieresis', 'Zcaron', 'zcaron', 'florin', 'circumflex', 'caron', 'breve', 'dotaccent', 'ring', 'ogonek', 'tilde', 'hungarumlaut', 'endash', 'emdash', 'quoteleft', 'quoteright', 'quotesinglbase', 'quotedblleft', 'quotedblright', 'quotedblbase', 'dagger', 'daggerdbl', 'bullet', 'ellipsis', 'perthousand', 'guilsinglleft', 'guilsinglright', 'fraction', 'Euro', 'trademark', 'minus']
    for gname in f.lib["public.glyphOrder"]:
        cg = f.newGlyph(gname)
        cg.appendComponent(elementName)
        cg.width = f[elementName].width
    f.autoUnicodes()
    f.save(path)
    f.close()
    
    
    ds += """
        <source familyname="%s" filename="%s" name="%s" stylename="%s">
            <location>""" %(series, fileName, sourceName, styleName)
    for listAxis in axes:
        if listAxis == 'origin' or listAxis == 'default':
            continue
        if listAxis == axis:
            listAxisValue = axisValue
        else:
            listAxisValue = 0
        ds += """
                <dimension name="%s" xvalue="%s" />""" % (listAxis, listAxisValue)
    
    ds +=  """
            </location>"""
    if axis == 'origin':
        ds += """
            <groups copy="1" />
            <features copy="1" />
            <info copy="1" />"""
    ds += """
        </source>"""

ds += """
    </sources>
    <instances></instances>
</designspace>
"""

with open(os.path.join(destBase, series+'.designspace'), 'w') as dsfile:
    dsfile.write(ds)

print ds