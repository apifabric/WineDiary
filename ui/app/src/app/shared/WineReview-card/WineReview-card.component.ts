import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './WineReview-card.component.html',
  styleUrls: ['./WineReview-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.WineReview-card]': 'true'
  }
})

export class WineReviewCardComponent {


}