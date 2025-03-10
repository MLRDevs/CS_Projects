// Alex Miller
// activity for a 1 fragment

package com.example.pg4_deviceslist

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.PersistableBundle
import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentActivity
import androidx.fragment.app.FragmentManager

abstract class SingleFragmentActivity : FragmentActivity() {
    protected abstract fun createFragment(): Fragment

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_fragment) // set the view to the right xml file
        val fm: FragmentManager? = supportFragmentManager // fragment manager is needed when dealing with fragments in an activity
        var fragment: Fragment? = fm!!.findFragmentById(R.id.fragment_container)
        if (fragment == null) { // if it doesn't find the fragment then just create a new one
            fragment = createFragment()
            fm.beginTransaction().add(R.id.fragment_container,fragment).commit()
        }
    }
}