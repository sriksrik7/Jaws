//
//  Locations.swift
//  Treker
//
//  Created by Anish Krishnamoorthy on 31/01/22.
//

import Foundation

class Locations :ObservableObject{
    let places: [Location]
    
    var primary: Location {
        places[0]
    }
    
    init() {
        let url = Bundle.main.url(forResource: "locations", withExtension: "json")!
        let data = try! Data(contentsOf: url)
        places = try! JSONDecoder().decode([Location].self, from: data)
    }
}
