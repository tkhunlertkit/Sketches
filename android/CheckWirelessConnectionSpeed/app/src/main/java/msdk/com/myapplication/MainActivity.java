package msdk.com.myapplication;

import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.support.annotation.NonNull;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import org.w3c.dom.Text;

public class MainActivity extends AppCompatActivity {

    private static final int CHECK_NETWORK_SPEED_KEY = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void checkConnectionSpeedClicked(View view) {
        String[] listOfPermissions = new String[]{Manifest.permission.ACCESS_NETWORK_STATE,
                                                Manifest.permission.ACCESS_WIFI_STATE};

        if (areAllPermissionsGranted(listOfPermissions)) {
            Toast.makeText(this, "Requesting Permission", Toast.LENGTH_SHORT).show();
            ActivityCompat.requestPermissions(this, listOfPermissions, CHECK_NETWORK_SPEED_KEY);
        } else {
            Toast.makeText(this, "all permissions granted", Toast.LENGTH_SHORT).show();
            checkConnectionSpeed();
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        switch (requestCode) {
            case CHECK_NETWORK_SPEED_KEY:
                if (grantResults.length > 0 && areAllPermissionsGranted(grantResults)) {
                    checkConnectionSpeed();
                }
                break;
            default: break;
        }
    }

    public boolean areAllPermissionsGranted(String[] listOfPermissions) {
        boolean result = true;
        for (String permission : listOfPermissions) {
            int currentPermissionState = ContextCompat.checkSelfPermission(this, permission);
            result = result && (currentPermissionState == PackageManager.PERMISSION_GRANTED);
        }
        return result;
    }

    public boolean areAllPermissionsGranted(int[] grantResults) {
        boolean result = true;
        for (int grant : grantResults) {
            result = result && grant == PackageManager.PERMISSION_GRANTED;
        }
        return result;

    }

    public void checkConnectionSpeed() {
        TextView tv = (TextView) findViewById(R.id.text1);
        ConnectivityManager cm = (ConnectivityManager) getSystemService(Context.CONNECTIVITY_SERVICE);
        NetworkInfo info = cm.getActiveNetworkInfo();

        String res = "";
        if (info != null) {
            res = "info is something\n";
            res += "Connectivity type: " + getConnectivityType(info.getType()) + "\n";
            if (info.getType() == ConnectivityManager.TYPE_WIFI) {
                res += "WIFI\n";
                WifiManager wm = (WifiManager) getSystemService(Context.WIFI_SERVICE);
                if (wm != null) {
                    WifiInfo wi = wm.getConnectionInfo();
                    int linkSpeed = wi.getLinkSpeed();

                    res += "SSID: " + wi.getSSID() + "\n";
                    res += "IP: " + wi.getIpAddress() + "\n";
                    res += linkSpeed + " " + WifiInfo.LINK_SPEED_UNITS + "\n";

                }
            } else {
                res += "This is NOT a Wifi Connection !!!\n";
            }
        } else {
            res = "info is null\n";
        }
        tv.setText(res);
    }

    public String getConnectivityType(int connectionType) {
        String res = "";
        switch (connectionType) {
            case ConnectivityManager.TYPE_BLUETOOTH:  res   = "Bluetooth";   break;
            case ConnectivityManager.TYPE_DUMMY:      res   = "Dummy";       break;
            case ConnectivityManager.TYPE_ETHERNET:   res   = "Ethernet";    break;
            case ConnectivityManager.TYPE_MOBILE:     res   = "Mobile";      break;
            case ConnectivityManager.TYPE_MOBILE_DUN: res   = "Mobile Dun?"; break;
            case ConnectivityManager.TYPE_VPN:        res   = "VPN";         break;
            case ConnectivityManager.TYPE_WIFI:       res   = "WIFI";        break;
            case ConnectivityManager.TYPE_WIMAX:      res   = "WiMax";       break;
            default: res = "Unknown Connectivity Type";
        }
        return res;
    }
}
