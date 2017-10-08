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
//        let vc = ViewController()
//        vc.imageView.image = UIImage(named: images[indexPath.row])
//        vc.imageName = images[indexPath.row]
//        present(vc, animated: false, completion: nil)
    }
}

