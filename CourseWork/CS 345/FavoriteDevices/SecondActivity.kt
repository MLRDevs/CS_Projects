// Alex Miller
// Second activity, get the company from the first activity and send back the device the user chooses
package com.example.pg3_favdevices

import android.content.Context
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.widget.Button

class SecondActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_second)

        // buttons for the devices
        var FirstButt:Button? = null
        var SecondButt: Button? = null
        var ThirdButt:Button? = null
        var FourthButt:Button? = null
        var FifthButt:Button? = null

        FirstButt = findViewById(R.id.FirstButt)
        SecondButt = findViewById(R.id.SecondButt)
        ThirdButt = findViewById(R.id.ThirdButt)
        FourthButt = findViewById(R.id.FourthButt)
        FifthButt = findViewById(R.id.FifthButt)

        // array of the buttons so less code when adding the right text to the buttons
        var Butts = arrayOf(FirstButt, SecondButt, ThirdButt, FourthButt, FifthButt)

        // all of the devices per Manufacturer
        var Apple = arrayOf("iPhone", "iPad", "iPod", "iPod mini", "Newton")
        var Samsung = arrayOf("Samsung Galaxy zfold", "Samsung Galaxy S24 ultra", "Samsung Galaxy A20", "Samsung Galaxy S23 FE", "Samsung Galaxy zflip")
        var Huawei = arrayOf("Huawei P60", "Huawei P50", "Huawei Mate 50 pro", "Huawei nova 11", "Huawei nova Y91")
        var Google = arrayOf("Google Pixel 8", "Google Pixel tablet", "Google Pixel 7a", "Google Pixel watch 2", "Google Pixel fold")
        var Blackberry = arrayOf("Blackberry Key2", "Blackberry Evolve X", "Blackberry Classic", "Blackberry passport", "Blackberry Aurora")

        // get the company
        var comp = intent.getStringExtra(EXTRA_COMP)

        // get the right text for the company onto the buttons
        if (comp == "Apple") {
            for (i in 0..4) Butts[i].text = Apple[i]
        }
        else if (comp == "Samsung") {
            for (i in 0..4) Butts[i].text = Samsung[i]
        }
        else if (comp == "Huawei") {
            for (i in 0..4) Butts[i].text = Huawei[i]
        }
        else if (comp == "Google") {
            for (i in 0..4) Butts[i].text = Google[i]
        }
        else if (comp == "Blackberry") {
            for (i in 0..4) Butts[i].text = Blackberry[i]
        }
        else { // else case for error checks
            for (i in 0..4) Butts[i].text = "ERROR"
        }

        // onclick events for the buttons
        FirstButt.setOnClickListener() {
            SendBackAns(FirstButt.text.toString())
        }
        SecondButt.setOnClickListener() {
            SendBackAns(SecondButt.text.toString())
        }
        ThirdButt.setOnClickListener() {
            SendBackAns(ThirdButt.text.toString())
        }
        FourthButt.setOnClickListener() {
            SendBackAns(FourthButt.text.toString())
        }
        FifthButt.setOnClickListener() {
            SendBackAns(FifthButt.text.toString())
        }
    }
    companion object {

        val EXTRA_COMP = "com.example.PG3_FavDevices.comp"
        val EXTRA_DEVICE = "com.example.PG3_FavDevices.device"

        // create the new intent
        fun newIntent(packageContext:Context?,comp:String):Intent? {
            var i:Intent? = Intent(packageContext,SecondActivity::class.java)
            i!!.putExtra(EXTRA_COMP,comp)
            return i
        }
        // return the device
        fun getAns(result:Intent?):String? {
            return result!!.getStringExtra(EXTRA_DEVICE)
        }
    }
    // save the device name and end this activity
    fun SendBackAns(ans:String) {
        var i:Intent? = Intent()
        i!!.putExtra(EXTRA_DEVICE,ans)
        setResult(RESULT_OK,i)
        finish()
    }
}