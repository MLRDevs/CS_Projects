// Alex Miller
// each fragment when you click into it

package com.example.pg4_deviceslist

import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import androidx.fragment.app.Fragment
import java.util.UUID

class DeviceFragment : Fragment() {
    // each variable in the device that will be shown
    var mDevice:Device? = null
    var mDeviceName: TextView? = null
    var mDeviceYear: TextView? = null
    var mDeviceRating: EditText? = null

    companion object {
        val DEVICE_ID = "device_id"

        fun newInstance (deviceID:UUID?):DeviceFragment {
            val args = Bundle()
            args.putSerializable(DEVICE_ID,deviceID)
            val fragment = DeviceFragment()
            fragment.arguments = args
            return fragment
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) { // create the activity
        super.onCreate(savedInstanceState)
        var deviceID:UUID? = requireArguments().getSerializable(DEVICE_ID) as UUID?
        mDevice = DeviceList.getDevice(deviceID)
    }

    override fun onCreateView( // creating the view
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {

        // put all the textviews with the appropriate xml code
        val v:View? = inflater.inflate(R.layout.fragment_device, container, false)
        mDeviceName = v!!.findViewById(R.id.device_title)
        mDeviceName!!.setText(mDevice!!.mDeviceName)
        mDeviceYear = v.findViewById(R.id.device_year)
        mDeviceYear!!.setText(mDevice!!.mDeviceYear)

        mDeviceRating = v.findViewById(R.id.device_rating)
        mDeviceRating!!.setText(mDevice!!.mDeviceRating.toString())
        mDeviceRating!!.addTextChangedListener(object: TextWatcher {
            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) { // what happens before the user changes the text

            }

            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) { // what happens as the user is changing the text
                if (s.toString() != "") {
                    mDevice!!.mDeviceRating = s.toString().toInt() // update the device rating when it changes, unless nothing is typed in
                }
            }

            override fun afterTextChanged(s: Editable?) { // what happens after user changes the text
                if (mDevice!!.mDeviceRating!! > 10 || s.toString() == "") { // rating has to be between 1-10
                    Toast.makeText(activity,"Rating must be between 1-10",Toast.LENGTH_SHORT).show()
                    mDevice!!.mDeviceRating = 1 // change it to 1 if it is
                }
                else { // otherwise just change it to the number the user entered
                    mDevice!!.mDeviceRating = s.toString().toInt()
                }

            }
        })

        return v // return the view
    }
}