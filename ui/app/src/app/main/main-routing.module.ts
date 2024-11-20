import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Person', loadChildren: () => import('./Person/Person.module').then(m => m.PersonModule) },
    
        { path: 'TastingSession', loadChildren: () => import('./TastingSession/TastingSession.module').then(m => m.TastingSessionModule) },
    
        { path: 'Wine', loadChildren: () => import('./Wine/Wine.module').then(m => m.WineModule) },
    
        { path: 'WineReview', loadChildren: () => import('./WineReview/WineReview.module').then(m => m.WineReviewModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }