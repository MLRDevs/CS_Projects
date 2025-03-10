// Alex Miller
// create the list of all the devices

package com.example.pg4_deviceslist

import java.util.UUID

object DeviceList {
    private val mDevices:MutableList<Device>?

    // names of all the devices, taken from PG3 to then loop through
    private var Apple = arrayOf("iPhone", "iPad", "iPod", "iPod mini", "Newton")
    private var Samsung = arrayOf("Samsung Galaxy zfold", "Samsung Galaxy S24 ultra", "Samsung Galaxy A20", "Samsung Galaxy S23 FE", "Samsung Galaxy zflip")
    private var Huawei = arrayOf("Huawei P60", "Huawei P50", "Huawei Mate 50 pro", "Huawei nova 11", "Huawei nova Y91")
    private var Google = arrayOf("Google Pixel 8", "Google Pixel tablet", "Google Pixel 7a", "Google Pixel watch 2", "Google Pixel fold")
    private var Blackberry = arrayOf("Blackberry Key2", "Blackberry Evolve X", "Blackberry Classic", "Blackberry passport", "Blackberry Aurora")

    // years when each device came out, only seen when clicked into the device for more info
    private var Years = arrayOf(
        "2007", "2010", "2001", "2004", "1987",
        "2019", "2024", "2019", "2023", "2020",
        "2023", "2021", "2022", "2023", "2023",
        "2023", "2023", "2023", "2023", "2023",
        "2018", "2018", "2014", "2014", "2017"
    )

    val devices:List<Device>?
        get() = mDevices

    fun getDevice (id: UUID?):Device? { // return the device with the right id
        for (device in mDevices!!)
            if (device.mId == id) return device
        return null
    }

    init { // create the devices and add them to the list
        mDevices = ArrayList()
        for (i in 0..24) { // for every device
            val device = Device()
            device.mDeviceYear = "Year made: " + Years[i]
            device.mDeviceRating = 1

            // if statements to go through each manufacturer to add the names, better than doing them all 1 by 1
            // could've done the same thing here I did with Years but already had the arrays from PG3
            if (i < 5) {
                device.mDeviceName = Apple[i]
            }
            else if (i < 10) {
                device.mDeviceName = Samsung[i-5]
            }
            else if (i < 15) {
                device.mDeviceName = Huawei[i-10]
            }
            else if (i < 20) {
                device.mDeviceName = Google[i-15]
            }
            else {
                device.mDeviceName = Blackberry[i-20]
            }
            mDevices.add(device) // add the device
        }
    }
}