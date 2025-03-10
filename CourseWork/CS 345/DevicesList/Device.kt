// Alex Miller
// what each device has
package com.example.pg4_deviceslist

import java.util.UUID

class Device {

    var mId: UUID? = UUID.randomUUID() // id
    var mDeviceName:String? = "" // name of the device
    var mDeviceYear:String? = "Year made: " // the year that it was made (only available on screen when user clicks into the device)
    var mDeviceRating:Int? = 1 // rating (set to 1 by default and when user inputs a rating outside of 1-10)
    // mDeviceRating is an int so in the xml it shows that only numbers can be correct input
}
