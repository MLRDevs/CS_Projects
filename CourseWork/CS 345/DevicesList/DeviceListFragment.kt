// Alex Miller
// handles the recycler view and what happens when user scrolls

package com.example.pg4_deviceslist

import android.content.Context
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import androidx.recyclerview.widget.LinearLayoutManager


class DeviceListFragment : Fragment() {
   private var mDeviceRecyclerView: RecyclerView? = null
   private var mAdapter: DeviceAdapter? = null

    override fun onCreateView( // creating the view
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view = inflater.inflate(R.layout.fragment_device_list, container, false)
        mDeviceRecyclerView = view.findViewById(R.id.device_recycler_view)
        mDeviceRecyclerView!!.layoutManager = LinearLayoutManager(activity) // making sure the layout is the right xml file
        updateUI() // update the ui
        return view
    }

    private fun updateUI() { // updating the ui
        val devicelist = DeviceList
        val devices = devicelist.devices
        if (mAdapter == null) { // if the adapter doesn't exist make a new one
            mAdapter = DeviceAdapter(devices)
            mDeviceRecyclerView!!.adapter = mAdapter
        }
        else {
            mAdapter!!.notifyDataSetChanged()
        }
    }

    private inner class DeviceHolder(itemView: View): RecyclerView.ViewHolder(itemView), View.OnClickListener { // required by recycler view, what happens when you click on the view
        private var mDevice:Device? = null
        private var mDeviceName: TextView? = null
        private var mDeviceRating: TextView? = null

        init { // connect xml to the variables
            itemView.setOnClickListener(this)
            mDeviceName = itemView.findViewById(R.id.list_item_device_name) as TextView
            mDeviceRating = itemView.findViewById(R.id.list_item_device_rating) as TextView
        }
        fun bindDevice(device: Device?) { // connect the stuff on screen to what the device has
            mDevice = device
            mDeviceName!!.text = mDevice!!.mDeviceName
            mDeviceRating!!.text = "Rating: " + mDevice!!.mDeviceRating.toString()
        }

        override fun onClick(v: View?) { // clicking on the view
            val intent = DevicePagerActivity.newIntent(activity as Context, mDevice!!.mId)
            startActivity(intent) // start the new activity for that device
        }
    }

    // adapter required for recycler view
    private inner class DeviceAdapter(private val mDevices: List<Device>?): RecyclerView.Adapter<DeviceHolder>() {
        override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): DeviceHolder {
            val layoutInflater = LayoutInflater.from(activity)
            val view = layoutInflater.inflate(R.layout.list_item_device, parent, false)
            return DeviceHolder(view)
        }

        override fun onDetachedFromRecyclerView(recyclerView: RecyclerView) { // when an item scrolls of the screen
            super.onDetachedFromRecyclerView(recyclerView)
        }

        override fun onBindViewHolder(holder: DeviceHolder, position: Int) { // when an item scrolls onto the screen
            val device = mDevices!![position]
            holder.bindDevice(device)
        }

        override fun getItemCount(): Int { // get size of devices in view
            return mDevices!!.size
        }
    }
    override fun onResume() { // when the activity resumes, update the ui
        super.onResume()
        updateUI()
    }
}