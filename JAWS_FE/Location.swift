//
//  Location.swift
//  Treker
//
//  Created by Anish Krishnamoorthy on 31/01/22.
//

import Foundation


struct Location: Decodable , Identifiable {
    let id: Int
    let name: String
    let country: String
    let description: String
    let more: String
    let latitude: Double
    let longitude: Double
    let heroPicture: String
    let advisory: String
    
    
   static let example = Location(id: 1, name: "Great Smoky Mountains", country: "United States", description: "A great Place to vist ", more: "More Text here", latitude: 35.5632, longitude: -83.4070, heroPicture: "smokies", advisory: "Beware of the bears")
}
