//
//  MapViewController.swift
//  Jaws
//
//  Created by Jaws Team.
//

import UIKit
import MapKit
import CoreLocation

class MapViewController: UIViewController,MKMapViewDelegate{
    @IBOutlet var MapView: MKMapView!
    
    
    let map = MKMapView()
//    let sa_data = ReadAttackData()
    let coordinate = CLLocationCoordinate2D(latitude: 40.728, longitude: -73)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.addSubview(map)
        map.frame = view.bounds
        
//        sa_data.sharkAttackData()
        
        map.setRegion(MKCoordinateRegion(center: coordinate, span: MKCoordinateSpan(latitudeDelta: 0.5, longitudeDelta: 0.5)), animated: false)
        
        map.delegate = self
        
        addCustomPin()

    }
    
    
    private func addCustomPin() {
        let pin = MKPointAnnotation()
        pin.coordinate = coordinate
        pin.title = "Shark"
        pin.subtitle = "Whale Shark"
        map.addAnnotation(pin)
        
    }
    
    private func MapView(_ MapView: MKMapView, viewFor annotation: MKAnnotation) -> MKAnnotationView? {
        guard !(annotation is MKUserLocation) else{
            return nil
        }
        
        var annotationView = map.dequeueReusableAnnotationView(withIdentifier: "custom")
        if annotation == nil{
            
            annotationView = MKAnnotationView(annotation: annotation, reuseIdentifier: "custom")
            annotationView?.canShowCallout = true
        }
        else{
            annotationView?.annotation = annotation
        }
        
        annotationView?.image = UIImage(named: "Whale Shark")
        
        return annotationView
        
    }
    

}
