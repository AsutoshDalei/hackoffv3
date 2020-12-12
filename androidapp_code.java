package com.example.buttoncontrol;

import android.graphics.Bitmap;
import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

import com.google.zxing.WriterException;

import androidmads.library.qrgenearator.QRGContents;
import androidmads.library.qrgenearator.QRGEncoder;

public class MainActivity extends AppCompatActivity {

    EditText qrValue;
    Button genBttn;
    ImageView qrImage;
    TextView flrText;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        qrValue = findViewById(R.id.qrInput);
        genBttn = findViewById(R.id.Gen);
        qrImage = findViewById(R.id.qrCode);
        flrText = findViewById(R.id.flrNum);

        genBttn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                flrText.setTextSize(24);
               String data = qrValue.getText().toString();
                if (data.isEmpty()){
                    qrValue.setError("Value Required.");
                }
                else{
                    QRGEncoder qrgEncoder = new QRGEncoder(data,null, QRGContents.Type.TEXT, 366);
                    Bitmap bitmap = qrgEncoder.getBitmap();
                    qrImage.setImageBitmap(bitmap);
                }
        }
        });
    }
}
