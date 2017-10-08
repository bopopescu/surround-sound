//
//  ViewController.swift
//  cameraApp
//
//  Created by Andrew Li on 10/7/17.
//  Copyright © 2017 Andrew Li. All rights reserved.
//

import UIKit

class ViewController: UIViewController, UINavigationControllerDelegate, UIImagePickerControllerDelegate {
    var imagePickerController : UIImagePickerController!

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : Any]) {
        imagePickerController.dismiss(animated: true, completion: nil)
        imageView.image = info[UIImagePickerControllerOriginalImage] as? UIImage
    }

    @IBOutlet weak var imageView: UIImageView!
    
    @IBAction func onPhotoButton(_ sender: Any) {
        imagePickerController = UIImagePickerController()
        imagePickerController.delegate = self
        imagePickerController.sourceType = .camera
        present(imagePickerController, animated: true, completion: nil)
    }
    
    @IBAction func onSaveButton(_ sender: Any) {
    }
    
    @IBAction func onGalleryButton(_ sender: Any) {
    }
}

