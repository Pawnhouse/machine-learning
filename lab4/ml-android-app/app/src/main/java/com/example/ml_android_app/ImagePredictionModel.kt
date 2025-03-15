package com.example.ml_android_app

import android.content.res.AssetFileDescriptor
import android.content.res.AssetManager
import android.graphics.Bitmap
import org.tensorflow.lite.Interpreter
import java.io.FileInputStream
import java.nio.MappedByteBuffer
import java.nio.channels.FileChannel


class ImagePredictionModel(assets: AssetManager) {
    companion object {
        private const val SVHN_MODEL_TFLITE = "svhn_model.tflite"
        private const val WIDTH = 32
        private const val HEIGHT = 32
    }

    private var tfliteModel: MappedByteBuffer

    init {
        tfliteModel = loadModelFile(assets)
    }

    private fun loadModelFile(assets: AssetManager): MappedByteBuffer {
        val fileDescriptor: AssetFileDescriptor = assets.openFd(SVHN_MODEL_TFLITE)
        val inputStream = FileInputStream(fileDescriptor.fileDescriptor)
        val fileChannel = inputStream.channel
        val startOffset = fileDescriptor.startOffset
        val declaredLength = fileDescriptor.declaredLength
        return fileChannel.map(FileChannel.MapMode.READ_ONLY, startOffset, declaredLength)
    }

    fun getPredictedDigit(bitmap: Bitmap): Int {
        val interpreter = Interpreter(tfliteModel)

        val input = preprocessImage(bitmap)
        val output = Array(1) { FloatArray(10) }

        interpreter.run(input, output)
        return output[0].indices.maxByOrNull { output[0][it] } ?: -1
    }

    private fun preprocessImage(bitmap: Bitmap): Array<Array<Array<FloatArray>>> {
        val resizedBitmap = Bitmap.createScaledBitmap(bitmap, WIDTH, HEIGHT, true)

        val input = Array(1) { Array(HEIGHT) { Array(WIDTH) { FloatArray(1) } } }

        for (i in 0 until HEIGHT) {
            for (j in 0 until WIDTH) {
                val pixel = resizedBitmap.getPixel(j, i)
                val gray = (0.299 * ((pixel shr 16) and 0xFF)
                        + 0.587 * ((pixel shr 8) and 0xFF)
                        + 0.114 * (pixel and 0xFF)).toFloat()
                input[0][i][j][0] = gray / 255.0f
            }
        }

        return input
    }
}