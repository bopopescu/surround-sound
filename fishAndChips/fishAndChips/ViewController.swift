//
//  ViewController.swift
//  fishAndChips
//
//  Created by Jiayue Li on 10/6/17.
//  Copyright © 2017 Jiayue Li. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    var auth = SPTAuth.defaultInstance()!
    var session:SPTSession!
    var player: SPTAudioStreamingController?
    var loginUrl: URL?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        setup()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func setup(){
        SPTAuth.defaultInstance().clientID = "41606d07c5f3410faa3c16c55a47b47f"
        SPTAuth.defaultInstance().redirectURL = URL(string: "8322cddac5804f24ae8eda242e09ef58")
        SPTAuth.defaultInstance().requestedScopes = [SPTAuthStreamingScope, SPTAuthPlaylistReadPrivateScope, SPTAuthPlaylistModifyPublicScope, SPTAuthPlaylistModifyPrivateScope]
        loginUrl = SPTAuth.defaultInstance().spotifyWebAuthenticationURL()
        
    }

    @IBAction func login(_ sender: Any) {
        UIApplication.shared.openURL(loginUrl!)
        
    }
    
    

}

