package com.example.pg4_deviceslist

import androidx.fragment.app.Fragment

class DeviceListActivity : SingleFragmentActivity() {
    override fun createFragment(): Fragment {
        return DeviceListFragment()
    }
}