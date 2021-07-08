grammar CatTasks;

catTasks: catTask*;

catTask: (detailed | nonDetailed) NL;

nonDetailed: action=NonWS WS
        task_id=NonWS WS
        parent_task_id=NonWS WS
        typefield=NonWS WS
        start_time=NonWS WS
        timestamp=NonWS WS
        running_time=NonWS WS
        ip=NonWS WS
        node=NonWS;

detailed: nonDetailed WS description;
description : (WS | NonWS)+;

WS: (' ')+;
NL: '\n';
NonWS: ~[ \n]+;