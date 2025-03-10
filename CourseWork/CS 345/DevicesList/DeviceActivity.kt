// Alex Miller
// creating the fragment

package com.example.pg4_deviceslist

import android.content.Context
import android.content.Intent
import androidx.fragment.app.Fragment
import java.util.UUID
import androidx.appcompat.app.AppCompatActivity

class DeviceActivity: SingleFragmentActivity() {
    companion object {
        val EXTRA_DEVICE_ID = "com.example.PG4-DeviceList.fragment1.deviceId"

        fun newIntent(packageContext: Context?, deviceID: UUID?): Intent { // create a new intent
            val intent = Intent(packageContext!!,DeviceActivity::class.java)
            intent.putExtra(EXTRA_DEVICE_ID,deviceID)
            return intent
        }
    }

    override fun createFragment(): Fragment { // create the fragment
        val deviceID: UUID? = intent.getSerializableExtra(EXTRA_DEVICE_ID) as UUID? // get the id
        return DeviceFragment.newInstance(deviceID) // return the new fragment
    }
}