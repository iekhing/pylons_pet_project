<%inherit file="/base.mako" />

<%def name="head_tags()">
  <!-- add some head tags here -->
</%def>

<h1>My Controller</h1>

<p>

% if c.loginStatus:
	welcome ${c.userId}!!!!	
% else:
	failed to login					
% endif						

		

</p>

