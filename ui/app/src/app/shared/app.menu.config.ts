import { MenuRootItem } from 'ontimize-web-ngx';

import { PersonCardComponent } from './Person-card/Person-card.component';

import { TastingSessionCardComponent } from './TastingSession-card/TastingSession-card.component';

import { WineCardComponent } from './Wine-card/Wine-card.component';

import { WineReviewCardComponent } from './WineReview-card/WineReview-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Person', name: 'PERSON', icon: 'view_list', route: '/main/Person' }
    
        ,{ id: 'TastingSession', name: 'TASTINGSESSION', icon: 'view_list', route: '/main/TastingSession' }
    
        ,{ id: 'Wine', name: 'WINE', icon: 'view_list', route: '/main/Wine' }
    
        ,{ id: 'WineReview', name: 'WINEREVIEW', icon: 'view_list', route: '/main/WineReview' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    PersonCardComponent

    ,TastingSessionCardComponent

    ,WineCardComponent

    ,WineReviewCardComponent

];