# -*- coding: utf-8 -*-

def urlmap(map, url_rules):
    " Util for make url rules easy "
    for rule in url_rules:
        params = {}
        
        if len(rule) == 2:
            url_pattern, controller_dot_action = rule
        elif len(rule) == 3:
            url_pattern, controller_dot_action, params = rule
        else:
            raise Exception('Wrong urlmap params!')
        
        controller, action = controller_dot_action.split('.')
        
        kwargs = {}
        kwargs.update(params)
        kwargs['controller'] = controller
        kwargs['action'] = action
        
        map.connect(None, url_pattern, **kwargs)