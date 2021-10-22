package config

var Upload uploader.TConfig

func InitUpload() {
	Upload = Config.Upload
}
