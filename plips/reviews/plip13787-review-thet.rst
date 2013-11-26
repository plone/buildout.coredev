PLIP 13787 Main Template / Barceloneta review
=============================================


General
-------

- Looks like a bit too early for a full review.

- Declare requirements of all direct imoprts in setup.py.

- PEP 8 everything.

- Mockup/Widgets integration and Javascript in general needs some more work.

- There should be a note in README.rst, how to install Barceloneta. Running 
  ``$ make bootstrap`` is required.

Clean theme
-----------

- Remove "base tag" rule in rules.xml.


Barceloneta theme
-----------------
  
  - The theme looks nice! It's Ploneish and doesn't look too similar to other
    designs. Altough, that's getting hard by depending on Bootstrap. However, I
    don't doubt this decision.

  - index.html: Resources should not be loaded from external sites (Yahoo,
    Bootstrap, Google).

  - rules.xml: Remove "base tag" rule in rules.xml.

  - The hero viewlet should only be visible for the start page. Also, I'm not
    sure, if we should use a viewlet here. They cannot be changed through the
    web, for example. Having the hero section within the content area would be
    more appropriate, in my opinion - or better yet but not in reach for Plone
    5: using tiles.

  - Search field's LSBox has width of 100%

  - ul#portal-globalnav should be wrapped within a <nav> element.

  - IMO, each column could be a "section" (column1-container,
    column2-container, content-container).

  - Wouldn't it be better to have each portlet wrapped in individual <aside>
    tags, contained within a <section> tag? I've done this for a client project
    like so:

..code-block XML::

      <!-- PORTLETS: wrap them in aside structure -->
      <xsl:template match="//div[@id='portal-column-two']/div[contains(@class, 'portletWrapper')]">
        <xsl:call-template name="portlet-aside-wrapper">
          <xsl:with-param name="hash" select="./@id"/>
          <xsl:with-param name="portlet" select="./dl"/>
        </xsl:call-template>
      </xsl:template>
      <xsl:template name="portlet-aside-wrapper">
        <xsl:param name="hash"/><!-- TODO: copy portlet hash to aside -->
        <xsl:param name="portlet"/>
        <aside>
          <h2><xsl:copy-of select="$portlet/dt/*"/></h2>
          <div class="portlet_body">
            <xsl:for-each select="$portlet/dd">
              <div class="block"><xsl:copy-of select="./*"/></div>
              <!-- TODO: add even|odd to class attr vals of div -->
            </xsl:for-each>
          </div>
        </aside>
      </xsl:template>


  - (In the long run, portlets itself should provide aside tags. Well, but then
    portlets already might be replaced by something better (tiles?).)

  - By the way, can't we rework the search field/search gadget? It's HTML
    Structure, espesially the LSResult's is far too complex and hard to theme.


Main Template
-------------

    - main_template.pt: XML TAL/METAL namespaces must be declared on very top
      of page.
    
    - ajax_main_template.pt: no TAL/METAL XML namespaces declared at all.
    
    - Why is the docttype defined via a tal:replace statement?
    
    - Baseslot can be dropped (also for ajax template...) 

    - AJAX main template in general: How is the AJAX main template going to be
      used? Browsers without Javascript support or links opened in a new window
      should still be served with the main_template as fallback.


Open for discussion
-------------------

- What about Bootstrap 3 in Barceloneta and Bootstrap 2 in p.a.widgets? Can
  p.a.widgets be migrated to use Bootstrap 3, including all of it's widgets?
  Can both coexist without interfering? It would be better to chose one
  framework and consistently use this one.

- Should Barceloneta really include it's own Toolbar? Maybe p.a.Toolbar can be
  made in a way to optionally work without an iframe, by having everything
  toolbar specific in an own namespace and strong CSS/jQuery selectors using
  this namespace. Or maybe the iframe thing isn't so much of an issue.





















