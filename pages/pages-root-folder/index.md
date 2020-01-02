---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: frontpage
header:
  image_fullwidth: header_unsplash_12.jpg
widget1:
  title: "英语学习"
  url: 'https://yyy18862325284.github.io/getting-started/'
  image: widget-1-302x182.jpg
  text: '工作中英语不仅要用在读上面，现在还需要<em>正常交流</em>，需要准确表达出工作中的内容，所以相信每天的进步会给将来带来不可小视的进步。'
widget2:
  title: "工作学习"
  url: 'http://localhost:4000/design/'
  text: '1. node <br/>1. python <br/>3. jsvascript<br/>4. docker <br/>5. nginx,...'
  video: '<a href="#" data-reveal-id="videoModal"><img src="http://phlow.github.io/feeling-responsive/images/start-video-feeling-responsive-302x182.jpg" width="302" height="182" alt=""/></a>'
widget3:
  title: "兴趣爱好"
  url: 'https://yyy18862325284.github.io/headers/'
  image: 333.png
  text: '没事多耍耍的爱好！'
#
# Use the call for action to show a button on the frontpage
#
# To make internal links, just use a permalink like this
# url: /getting-started/
#
# To style the button in different colors, use no value
# to use the main color or success, alert or secondary.
# To change colors see sass/_01_settings_colors.scss
#
callforaction:
  url: https://tinyletter.com/feeling-responsive
  text: Inform me about new updates and features ›
  style: alert
permalink: /index.html
#
# This is a nasty hack to make the navigation highlight
# this page as active in the topbar navigation
#
homepage: true
---

<div id="videoModal" class="reveal-modal large" data-reveal="">
  <div class="flex-video widescreen vimeo" style="display: block;">
    <iframe width="1280" height="720" src="https://www.youtube.com/embed/3b5zCFSmVvU" frameborder="0" allowfullscreen></iframe>
  </div>
  <a class="close-reveal-modal">&#215;</a>
</div>
