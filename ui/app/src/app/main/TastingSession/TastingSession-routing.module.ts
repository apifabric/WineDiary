import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TastingSessionHomeComponent } from './home/TastingSession-home.component';
import { TastingSessionNewComponent } from './new/TastingSession-new.component';
import { TastingSessionDetailComponent } from './detail/TastingSession-detail.component';

const routes: Routes = [
  {path: '', component: TastingSessionHomeComponent},
  { path: 'new', component: TastingSessionNewComponent },
  { path: ':id', component: TastingSessionDetailComponent,
    data: {
      oPermission: {
        permissionId: 'TastingSession-detail-permissions'
      }
    }
  }
];

export const TASTINGSESSION_MODULE_DECLARATIONS = [
    TastingSessionHomeComponent,
    TastingSessionNewComponent,
    TastingSessionDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TastingSessionRoutingModule { }