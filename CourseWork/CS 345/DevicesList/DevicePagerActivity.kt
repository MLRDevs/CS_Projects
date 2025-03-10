// Alex Miller
// sets the page viewer to be able to see different devices when user scrolls

package com.example.pg4_deviceslist

import android.content.Context
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.fragment.app.Fragment
import androidx.viewpager2.adapter.FragmentStateAdapter
import androidx.viewpager2.widget.ViewPager2
import com.example.pg4_deviceslist.DeviceActivity.Companion.EXTRA_DEVICE_ID
import java.util.UUID

class DevicePagerActivity : AppCompatActivity() {

    private var mViewPager: ViewPager2? = null
    private var mDevices:List<Device>? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_device_pager) // set the layout to the specific xml file
        val deviceId = intent.getSerializableExtra(EXTRA_DEVICE_ID) as UUID
        mViewPager = findViewById(R.id.device_view_pager) // get the view
        mDevices = DeviceList.devices // get the list of devices
        val fragmentManager = supportFragmentManager // dealing with fragments in an activity so fragment manager is needed

        mViewPager!!.adapter = object: FragmentStateAdapter(fragmentManager, lifecycle) {
            override fun createFragment(position: Int): Fragment { // creating the fragment for the specific device
                val device = mDevices!![position] // get the device in the current position
                return DeviceFragment.newInstance(device.mId) // create the new fragment
            }

            override fun getItemCount(): Int { // getting the count of the devices
                return mDevices!!.size
            }
        }

        for (i in mDevices!!.indices) { // where we are inside of the view
            if (mDevices!![i].mId == deviceId) {
                mViewPager!!.currentItem = i
                break
            }
        }
    }
    companion object {
        fun newIntent (packageContext: Context, deviceId:UUID?): Intent { // create a new intent
            val intent = Intent(packageContext, DevicePagerActivity::class.java)
            intent.putExtra(EXTRA_DEVICE_ID,deviceId)
            return intent
        }
    }
}