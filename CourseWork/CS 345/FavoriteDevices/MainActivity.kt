// Alex Miller
// select a company and then select a device from that company, then show the selected device on the main activity
package com.example.pg3_favdevices

import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.activity.result.contract.ActivityResultContracts

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // buttons for each manufacturer
        var AppleButt: Button? = null
        var SamsungButt:Button? = null
        var HuaweiButt:Button? = null
        var GoogleButt:Button? = null
        var BlackberryButt:Button? = null
        var mText: TextView? = null

        AppleButt = findViewById(R.id.AppleButt)
        SamsungButt = findViewById(R.id.SamsungButt)
        HuaweiButt = findViewById(R.id.HuaweiButt)
        GoogleButt = findViewById(R.id.GoogleButt)
        BlackberryButt = findViewById(R.id.BlackberryButt)
        mText = findViewById(R.id.Text)

        // when we get the device name, put it in the textview
        val resultLauncher = registerForActivityResult (ActivityResultContracts.StartActivityForResult ()) { result ->
            if (result.resultCode == Activity.RESULT_OK) {
                var data: Intent? = result.data
                if (data == null) mText.text = "ERROR" // error checking
                else mText.text = "your favorite device is the " + SecondActivity.getAns(data) + " pick another:"
            }
        }

        // sending the intent
        fun SendIntent(comp:String) {
            var i:Intent? = null
            i = SecondActivity.newIntent(this,comp)
            resultLauncher.launch(i)
        }

        // each manufacturer button
        AppleButt!!.setOnClickListener() {
            SendIntent("Apple")
        }
        SamsungButt!!.setOnClickListener() {
            SendIntent("Samsung")
        }
        HuaweiButt!!.setOnClickListener() {
            SendIntent("Huawei")
        }
        GoogleButt!!.setOnClickListener() {
            SendIntent("Google")
        }
        BlackberryButt!!.setOnClickListener() {
            SendIntent("Blackberry")
        }

    }
}