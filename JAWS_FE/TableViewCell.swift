//
//  TableViewCell.swift
//  JAWS_UI
//
//  Created by Anish Krishnamoorthy on 23/03/22.
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
