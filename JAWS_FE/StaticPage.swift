//
//  ViewController.swift
//  JAWS_UI
//
//  Created by Anish Krishnamoorthy on 23/03/22.
//

import UIKit

class StaticPage: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    
    @IBOutlet var tableView: UITableView!
    
    let Title = [("Bull Shark"),("Great White Shark"),("Hammer Head Shark"),("Megamouth Shark"),("Whale Shark")]
    
    let Text = [("The bull shark (Carcharhinus leucas), also known as the \"Zambezi shark\" (informally \"zambi\") in Africa and \"Lake Nicaragua shark\" in Nicaragua is a requim Shark commonly found worldwide in warm, shallow waters along coasts and in rivers. It is known for its aggressive nature, and presence in warm,shallow brackish and freshwater system including estuaries and rivers Bull sharks can thrive in both salt and fresh water and can travel far up rivers. They have been known to travel up the Mississippi River as far as Alton, Illinoisabout 1,100 kilometres (700 mi) from the ocean. However, few freshwater human-shark interactions have been recorded. Larger-sized bull sharks are probably responsible for the majority of near-shore shark attacks, including many bites attributed to other species. "),
    
                ("The great white shark (Carcharodon carcharias), also known as the white shark, white pointer, or simply great white, is a species of large mackerel shark which can be found in the coastal surface waters of all the major oceans. It is notable for its size, with larger female individuals growing to 6.1 m (20 ft) in length and 1,905–2,268 kg (4,200–5,000 lb) in weight at maturity.However, most are smaller; males measure 3.4 to 4.0 m (11 to 13 ft), and females measure 4.6 to 4.9 m (15 to 16 ft) on average.According to a 2014 study, the lifespan of great white sharks is estimated to be as long as 70 years or more, well above previous estimates,making it one of the longest lived cartilaginous fishes currently known.According to the same study, male great white sharks take 26 years to reach sexual maturity, while the females take 33 years to be ready to produce offspring.Great white sharks can swim at speeds of 25 km/hr (16 mph)for short bursts and to depths of 1,200 m (3,900 ft)."),
                ("The hammerhead sharks are a group of sharks that form the family Sphyrnidae, so named for the unusual and distinctive structure of their heads, which are flattened and laterally extended into a \"hammer\" shape called a cephalofoil. Most hammerhead species are placed in the genus Sphyrna, while the winghead shark is placed in its own genus, Eusphyra. Many different, but not necessarily mutually exclusive, functions have been postulated for the cephalofoil, including sensory reception, manoeuvering, and prey manipulation. The cephalofoil gives the shark superior binocular vision and depth perception.Hammerheads are found worldwide in warmer waters along coastlines and continental shelves. Unlike most sharks, some hammerhead species usually swim in schools during the day, becoming solitary hunters at night. Some of these schools can be found near Malpelo Island in Colombia, the Galápagos Islands in Ecuador, Cocos Island off Costa Rica, near Molokai in Hawaii, and off southern and eastern Africa."),
                ("The megamouth shark (Megachasma pelagios) is a species of deepwater shark. It is rarely seen by humans and is the smallest of the three extant filter-feeding sharks alongside the whale shark and basking shark. Since its discovery in 1976, fewer than 100 specimens have been observed or caught.[2] Like the other two planktivorous sharks, it swims with its mouth wide open, filtering water for plankton and jellyfish. It is recognizable from its large head with rubbery lips. The megamouth is so unlike any other type of shark that it is usually considered to be the sole extant species in the family Megachasmidae, though some scientists have suggested it may belong in the family Cetorhinidae, of which the basking shark is currently the sole extant member"),
                ("The whale shark (Rhincodon typus) is a slow-moving, filter-feeding carpet shark and the largest known extant fish species. The largest confirmed individual had a length of 18.8 m (61.7 ft).The whale shark holds many records for size in the animal kingdom, most notably being by far the largest living nonmammalian vertebrate. It is the sole member of the genus Rhincodon and the only extant member of the family Rhincodontidae, which belongs to the subclass Elasmobranchii in the class Chondrichthyes. Before 1984 it was classified as Rhiniodon into Rhinodontidae.The whale shark is found in open waters of the tropical oceans and is rarely found in water below 21 °C (70 °F).Studies looking at vertebral growth bands and the growth rates of free-swimming sharks have estimated whale shark lifespans at 80–130 years.Whale sharks have very large mouths and are filter feeders, which is a feeding mode that occurs in only two other sharks, the megamouth shark and the basking shark. They feed almost exclusively on plankton and small fishes, and pose no threat to humans.")]
    
    let imagesS = [UIImage(named: "Bull Shark"),
                    UIImage(named: "Great White Shark"),
                    UIImage(named: "Hammer Head Shark"),
                    UIImage(named: "Megamouth Shark"),
                    UIImage(named: "Whale Shark")]
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        tableView.delegate = self
        tableView.dataSource = self
        
    }
    
    func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return Title.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath as IndexPath) as! TableViewCell
        cell.imageCell.image = self.imagesS[indexPath.row]
        cell.titleLabel01.text = self.Title[indexPath.row]
        cell.textLabel02.text = self.Text[indexPath.row]
        
        return cell
    }


}

