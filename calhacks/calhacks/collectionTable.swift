//
//  collectionTable.swift
//  calhacks
//
//  Created by Sera Yang on 10/8/17.
//  Copyright © 2017 com.calhacks. All rights reserved.
//

import Foundation
import UIKit

class collectionTable : UIViewController, UICollectionViewDelegate, UICollectionViewDataSource{
    
    @IBOutlet weak var collectionView: UICollectionView!
    var images = ["Ny", "Party", "Study", "Us", "Rain"]
    var imglink = ["https://www.nycgo.com/images/uploads/homepage/Empire-State-Building-Observatory-Tom-Perry-2618.jpg", "https://vergecampus.com/wp-content/uploads/2015/06/college-dance-party.jpg", "https://www.cmich.edu/ess/studentaffairs/SDS/PublishingImages/good-study-habits.png","https://scontent.fsnc1-1.fna.fbcdn.net/v/t1.0-9/18671007_1304461276256308_665212443547993062_n.jpg?oh=9e764d5f13eca9cc1e22dec5234656cc&oe=5A72AD96", "https://static.pexels.com/photos/7816/pexels-photo.jpg"]
    var spotify = ["https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX0XUsuxWHRQd", "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXcBWIGoYBM5M", "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX4sWSpwq3LiO","https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXcBWIGoYBM5M","https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX4WYpdgoIcn6"]
    
    override func viewDidLoad() {
        self.collectionView.allowsSelection = true
        super.viewDidLoad()
        collectionView.delegate = self
        collectionView.dataSource = self
    }
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return images.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "CustomCell", for: indexPath) as! collectionCell
        
        cell.myImage.image = UIImage(named: images[indexPath.row])
        
        return cell
    }
    
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        print(images[indexPath.row])
        
    
           UIApplication.shared.openURL(NSURL(string:self.spotify[indexPath.row])! as URL)
        
        
//        let storyboard = UIStoryboard(name: "ViewController", bundle: nil)
//        let controller = storyboard.instantiateViewController(withIdentifier: "ViewController") as! ViewController
//        controller.imageName = images[indexPath.row]
//        controller.spotify = self.spotify[indexPath.row]
//        self.present(controller, animated: true, completion: nil)
    }
    
    
    
}

