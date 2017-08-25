import re

def clean_paste(data):

    data = re.sub(r'<!DOCTYPE html>\n<html lang="en" dir="ltr" prefix="og: http://ogp.me/ns# article: http://ogp.me/ns/article# book: http://ogp.me/ns/book# profile: http://ogp.me/ns/profile# video: http://ogp.me/ns/video# product: http://ogp.me/ns/product# content: http://purl.org/rss/1.0/modules/content/ dc: http://purl.org/dc/terms/ foaf: http://xmlns.com/foaf/0.1/ rdfs: http://www.w3.org/2000/01/rdf-schema# sioc: http://rdfs.org/sioc/ns# sioct: http://rdfs.org/sioc/types# skos: http://www.w3.org/2004/02/skos/core# xsd: http://www.w3.org/2001/XMLSchema#">\n<head>\n'                                                                                                                                         
                        , r'<?xml version="1.0" encoding="UTF-8" ?>\r\t<rss version="2.0"\r\txmlns:excerpt="http://wordpress.org/export/1.2/excerpt/"\r\txmlns:content="http://purl.org/rss/1.0/modules/content/"\r\txmlns:wfw="http://wellformedweb.org/CommentAPI/"\r\txmlns:dc="http://purl.org/dc/elements/1.1/"\r\txmlns:wp="http://wordpress.org/export/1.2/"\r\t>\r\t<channel>\r\t\t<title>Hakai Magazine</title>\r\t\t<link>http://hakaimagazine.com</link>\r\t\t<description>Coastal science and societies</description>\r\t\t<pubDate>Wed, 23 Aug 2017 22:09:13 +0000</pubDate>\r\t\t<language>en-US</language>\r\t\t<wp:wxr_version>1.2</wp:wxr_version>\r\t\t<wp:base_site_url>http://hakaimagazine.com</wp:base_site_url>\r\t\t<wp:base_blog_url>http://hakaimagazine.com</wp:base_blog_url>\r\t\t<wp:author>\r\t\t\t<wp:author_id>1</wp:author_id>\r\t\t\t<wp:author_login><![CDATA[hakaimagazine]]></wp:author_login>\r\t\t\t<wp:author_email><![CDATA[info@hakaimagazine.com]]></wp:author_email>\r\t\t\t<wp:author_display_name><![CDATA[hakaimagazine]]></wp:author_display_name>\r\t\t\t<wp:author_first_name><![CDATA[Hakai]]></wp:author_first_name>\r\t\t\t<wp:author_last_name><![CDATA[Magazine]]></wp:author_last_name>\r\t\t</wp:author>\r\t\t<generator>https://wordpress.org/?v=4.8</generator>\r\t\t\r\t\t<item>', data)
    data = re.sub(r'  <meta http-equiv="Content-Type" content="text\/html; charset=utf-8" \/><script type="text\/javascript">.*<\/script>\n'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                        , r'<junktagstart>', data)
    data = re.sub(r'<meta name="twitter:image" content="(.*)" />'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                        , r'<junktagend>', data)
    data = re.sub(r'<junktagstart>[\s\S]*<junktagend>'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                        , r'\r', data)
    data = re.sub(r'  <title>(.*) \| Hakai Magazine</title>\n'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                        , r'\r\t\t<title>\1</title>\r\t\t<dc:creator><![CDATA[hakaimagazine]]></dc:creator>\r\t\t<description></description>\r<junktagstart>', data)
    data = re.sub(r'<h2><div class="field field-name-field-dek field-type-text-long field-label-hidden"><div class="field-items"><div class="field-item even"><p>(.*)</p>'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                        , r'<junktagend>\t\t<excerpt:encoded><![CDATA[\1]]></excerpt:encoded>\r\t\t<wp:postmeta>\r\t\t\t<wp:meta_key><![CDATA[deck]]></wp:meta_key>\r\t\t\t<wp:meta_value><![CDATA[\1]]></wp:meta_value>\r\t\t</wp:postmeta><junktagstart>', data)
    data = re.sub(r'<junktagstart>[\s\S]*<junktagend>'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                        , r'\r', data)
    data = re.sub(r'       <span class="byline__group"><span class="byline__what">(.*)</span> <span class="byline__who">(.*)</span></span>     </div>'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                        , r'', data)
    data = re.sub(r'</div> <div class="field field-name-field-date-published field-type-datetime field-label-hidden"><div class="field-items"><div class="field-item even"><span class="date-display-single" property="dc:date" datatype="xsd:dateTime" content="(.*)T(.*)">Published (.*)</span></div></div></div><div class="field field-name-field-body field-type-text-long field-label-hidden"><div class="field-items"><div class="field-item even">'                                                                                                                                                                                                                                                                                  
                        , r'<junktagend>\r\t\t<wp:post_date><![CDATA[\1 00:00:00]]></wp:post_date>\r\t\t<wp:post_date_gmt><![CDATA[\1 00:00:00]]></wp:post_date_gmt>\r\t\t<wp:ping_status><![CDATA[closed]]></wp:ping_status>\r\t\t<wp:status><![CDATA[publish]]></wp:status>\r\t\t<wp:post_parent>0</wp:post_parent>\r\t\t<wp:menu_order>0</wp:menu_order><contentstartinghere>', data)
    data = re.sub(r'<junktagstart>[\s\S]*<junktagend>'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                        , r'\r', data)
    data = re.sub(r'<contentstartinghere>'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                        , r'\r\t\t<content:encoded><![CDATA[', data)
    data = re.sub(r'</div></div></div><div class="field field-name-field-share-buttons field-type-blockreference field-label-hidden">'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                        , r'\r\t\t]]></content:encoded><junktagstart>', data)

    data = re.sub(r'<div class="views-field views-field-field-geographic-region"><span class="views-label views-label-field-geographic-region">Geographic Region: </span><div class="field-content"><a href="/geographic-region/(.*)" typeof="skos:Concept" property="rdfs:label skos:prefLabel" datatype="">(.*)</a></div></div>      '                                                                                                                                                                                                                                                                                                                                                                                             
                        , r'<junktagend>\t\t<category domain="geographicregion" nicename="\1"><![CDATA[\2]]></category>', data)
    data = re.sub(r'<junktagstart>[\s\S]*<junktagend>'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                        , r'\r', data)
    data = re.sub(r'<div class="views-field views-field-field-oceanographic-region"><span class="views-label views-label-field-oceanographic-region">Oceanographic Region: </span><div class="field-content"><a href="/oceanographic-region/(.*)" typeof="skos:Concept" property="rdfs:label skos:prefLabel" datatype="">(.*)</a></div></div>'                                                                                                                                                                                                                                                                                                                                                                                 
                        , r'\r\t\t<category domain="oceanographicregion" nicename="\1"><![CDATA[\2]]></category>', data)
    data = re.sub(r'<div class="article-metadata-right views-fieldset" data-module="views_fieldsets">'                                                                                                                                                                                                                                                                                                                                                                                                                        
                        , r'\r', data)
    data = re.sub(r'      <div class="views-field views-field-field-species"><span class="views-label views-label-field-species">Species: </span><div class="field-content">'                                                                                                                                                                                                                                                                                                                                                                                                                        
                        , r'\r', data)    
    data = re.sub(r'<a href="/species/([a-zA-Z\s\-]*)" typeof="skos:Concept" property="rdfs:label skos:prefLabel" datatype="">([a-zA-Z\s\-]*)</a>'
                        , r'\r\t\t<category domain="species" nicename="\1"><![CDATA[\2]]></category>\r', data)
    data = re.sub(r'</div></div>      <div class="views-field views-field-field-scifield-discipline"><span class="views-label views-label-field-scifield-discipline">Scientific Fields: </span><div class="field-content">'                                                                                                                                                                                                                                                                                                                                                                                                                        
                        , r'\r', data)
    data = re.sub(r'<a href="/scientific-fielddiscipline/([a-zA-Z\s\-]*)" typeof="skos:Concept" property="rdfs:label skos:prefLabel" datatype="">([a-zA-Z\s\-]*)</a>'
                         , r'\r\t\t<category domain="discipline" nicename="\1"><![CDATA[\2]]></category>\r</item>\r</channel>\r</rss>\r<endoffile>', data)
    data = re.sub(r'<endoffile>[\s\S]*'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
                        , r'', data)
    return data
