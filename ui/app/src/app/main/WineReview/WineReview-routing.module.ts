import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WineReviewHomeComponent } from './home/WineReview-home.component';
import { WineReviewNewComponent } from './new/WineReview-new.component';
import { WineReviewDetailComponent } from './detail/WineReview-detail.component';

const routes: Routes = [
  {path: '', component: WineReviewHomeComponent},
  { path: 'new', component: WineReviewNewComponent },
  { path: ':id', component: WineReviewDetailComponent,
    data: {
      oPermission: {
        permissionId: 'WineReview-detail-permissions'
      }
    }
  }
];

export const WINEREVIEW_MODULE_DECLARATIONS = [
    WineReviewHomeComponent,
    WineReviewNewComponent,
    WineReviewDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WineReviewRoutingModule { }