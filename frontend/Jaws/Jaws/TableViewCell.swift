//
//  TableViewCell.swift
//  Jaws
//
//  Created by Jaws Team.
//

import UIKit

class TableViewCell: UITableViewCell {

    @IBOutlet var imageCell: UIImageView!
    @IBOutlet var titleLabel01: UILabel!
    @IBOutlet var textLabel02: UILabel!
    
    
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
