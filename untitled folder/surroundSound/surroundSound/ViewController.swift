//
//  ViewController.swift
//  surroundSound
//
//  Created by Jiayue Li on 10/7/17.
//  Copyright © 2017 Jiayue Li. All rights reserved.
//

import UIKit
import Foundation

class ViewController: UIViewController, UINavigationControllerDelegate, UIImagePickerControllerDelegate{

    var imagePickerController : UIImagePickerController!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        var request = URLRequest(url: URL(string: "https://utility-zenith-182301.appspot.com/topic")!)
        request.httpMethod = "POST"
        let dict = ["hello": "world"]
        let jsonData = try? JSONSerialization.data(withJSONObject: dict)
        request.setValue("application/json; charset=utf-8", forHTTPHeaderField: "Content-type")
        request.httpBody = jsonData
        let task = URLSession.shared.dataTask(with: request) { data, response, error in
            guard let data = data, error == nil else {                                                 // check for fundamental networking error
                print("error=\(error)")
                return
            }
            
            if let httpStatus = response as? HTTPURLResponse, httpStatus.statusCode != 200 {           // check for http errors
                print("statusCode should be 200, but is \(httpStatus.statusCode)")
                print("response = \(response)")
            }
            
            let responseString = String(data: data, encoding: .utf8)
            print("responseString = \(responseString)")
            let res = self.convertToDictionary(text: responseString!)
            let resdict = res as! [String:Any]
            print(resdict)
        }
        task.resume()
        
        // Set the URL the request is being made to.
//        let request = URLRequest(url: NSURL(string: "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")! as URL)
//        do {
//            // Perform the request
//            var response: AutoreleasingUnsafeMutablePointer<URLResponse?>? = nil
////            let data1 = try NSURLConnection.
//            let data = try NSURLConnection.sendSynchronousRequest(request, returning: response)
//            
//            // Convert the data to JSON
//            let jsonSerialized = try JSONSerialization.jsonObject(with: data, options: []) as? [String : Any]
//            
//            if let json = jsonSerialized, let url = json["url"], let explanation = json["explanation"] {
//                print(url)
//                print(explanation)
//            }
//        }
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func open(_ sender: Any) {
        UIApplication.shared.openURL(NSURL(string:"https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWYBO1MoTDhZI")! as URL)
    }

    func convertToDictionary(text: String) -> [String: Any]? {
        if let data = text.data(using: .utf8) {
            do {
                return try JSONSerialization.jsonObject(with: data, options: []) as? [String: Any]
            } catch {
                print(error.localizedDescription)
            }
        }
        return nil
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

